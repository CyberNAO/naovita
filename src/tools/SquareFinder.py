'''
Created on 9 juin 2011

@author: Bruno Barbieri
'''
from tools import Imagerie, Deplacements
import Image
import ImageFilter
import ImageChops
import operator

class SquareFinder:
    def __init__(self, connection):
        '''
        Constructor
        '''
        #self.__camProxy = connection.getProxy('ALVideoDevice')
        self.__imagerie = Imagerie.Imagerie(connection)
        
        self.__walk = Deplacements.Deplacements(connection)
        
    def recon_old(self, firstTime):
        self.__walk.poseInit()
        if firstTime:
            angle = self.orient()
            if angle != None :
                return angle
        
        self.__walk.bendHead()
        angle = self.orient()
        if angle != None :
            self.__walk.raiseHead()
            return angle
        
        self.__walk.raiseHead()
        
        self.__walk.kneel()
        angle = self.orient()
        
        self.__walk.standUp()
        return angle
        #penser a tourner brusquement si y'a rien devant.


    def MYrecon(self, color):
        im = self.__imagerie.getImage()

        width, height = im.size
        squares, dists = self.findSquares(im, color)
        
        dir = None
        limit = width/8
        if len(dists) != 0:            
            if abs(dists[0]) < limit:
                #print("IT'S JUST IN FRONT OF US !!!")
                dir = 0
            elif dists[0] < 0:
                #print("TO THE LEFT !!!!")
                dir = 1
            else:
                #print("TO THE RIGHT !!!!")
                dir = -1
                
        
        return {color : (dir, len(squares)) }
        #self.cropSquares(squares, im)

    def recon(self, color):
        im = self.__imagerie.getImage()

        width, height = im.size
        squares, dists = self.findSquares(im, color)
        
        dir = None
        limit = width/8
        if len(dists) != 0:            
            if abs(dists[0]) < limit:
                #print("IT'S JUST IN FRONT OF US !!!")
                dir = 0
            elif dists[0] < 0:
                #print("TO THE LEFT !!!!")
                dir = 1
            else:
                #print("TO THE RIGHT !!!!")
                dir = -1
                
        range = None
        if dir != None and color == "red" :
            range = self.getRange(len(squares[0]))
            
        return {color : (dir, len(squares), range) }
        #self.cropSquares(squares, im)
    
    def getRange(self, area):
        if area < 250 :
            return 6.0
        elif area >= 250 and area < 900 :
            return 3.0
        elif area >= 900 :
            return 2.0
    
    def orient(self, color):
        im = self.__imagerie.getImage()

        width, height = im.size
        squares, dists = self.findSquares(im, color)
        
        dir = None
        limit = width/8
        if len(dists) != 0:            
            if abs(dists[0]) < limit:
                #print("IT'S JUST IN FRONT OF US !!!")
                dir = 0
            elif dists[0] < 0:
                #print("TO THE LEFT !!!!")
                dir = 1
            else:
                #print("TO THE RIGHT !!!!")
                dir = -1
                
        
        return {color : dir}
        #self.cropSquares(squares, im)
                
    def cropSquares(self, squares, im):
        #crop the squares
        num = 0
        print("--------------------------------cropping " + str(len(squares)) + " square regions")
        for square in squares:
            imgSquare = self.regionCropper(square, im)
            imgSquare.save("squareTest" + str(num) + ".png")
            num += 1

#takes a binary image plan and returns the regions, i.e. the groups of connected points
    def regionFinder(self, image):
        width, height = image.size
        regions = []
        points = []
        for x in range(width):
            pointrow = []
            for y in range(height):
                pointrow.append(0 != image.getpixel((x,y)))
            points.append(pointrow)
        
        
        imageSize = width*height
        
        for x in range(width):
            for y in range(height):
                if (points[x][y]):
                    neighbours = []
                    neighbours.append([x,y])
                    
                    region = []
                    
                    while len(neighbours) > 0:
                        point = neighbours.pop()
                        region.append(point)
                        for neighbour in self.getNeighbours(point, width, height, points):
                            neighbours.append(neighbour)
                            points[neighbour[0]][neighbour[1]] = False
                    #tests on the region size
                    if len(region)>imageSize/1000 and len(region)<imageSize/10:
                        regions.append(region)
        return regions
    
    #gets the neighbours of a point
    def getNeighbours(self, point, width, height, points):
        neighbours = []
        if (point[0] < width - 1) and points[point[0]+1][point[1]]:
            neighbours.append([point[0]+1, point[1]])
        if (point[1] < height - 1) and points[point[0]][point[1]+1]:
            neighbours.append([point[0], point[1]+1])
        if (point[0] > 0) and points[point[0]-1][point[1]]:
            neighbours.append([point[0]-1, point[1]])
        if (point[1] > 0) and points[point[0]][point[1]-1]:
            neighbours.append([point[0], point[1]-1])
        return neighbours
    
    #find the convex hull of a region
    def findConvexHull(self, region, height):
        hull = []
        
        min = height
        for point in region:
            if point[1] < min:
                min = point[1]
                minPoint = point
                
        curPoint = minPoint
        hull.append(curPoint)
        
        curPoint = self.findPoint(region, curPoint)
        hull.append(curPoint)
        
        while curPoint != minPoint:
            curPoint = self.findPoint(region, curPoint)
            hull.append(curPoint)
            
        return hull
    
    def signum(self, int):
        if(int < 0):
            return -1;
        elif(int > 0):
            return 1;
        else:
            return int;
    
    def findPoint(self, points, start):
        if points[0] == start:
            end = points[1]
        else:
            end = points[0]
        for point in points:
            if (point != start) and (point != end):
                position = self.signum((end[0] - start[0]) * (point[1] - start[1]) - (end[1] - start[1]) * (point[0] - start[0]))
                if position > 0:
                    end = point
        return end
    
    #square distance
    def dist(self, point1, point2):
        dx = abs(point1[0] - point2[0])
        dy = abs(point1[1] - point2[1])
        return dx*dx + dy*dy
    
    #finds the biggest diagonal (the biggest distance between two points in the polygon) and returns the two points
    def findBiggestDiagonal(self, polygon):
        maxDiag1 = (polygon[0], polygon[1])
        max1 = self.dist(polygon[0], polygon[1])
        
        for i in range(len(polygon)-1):
            for j in range(i+1,len(polygon)):
                point1 = polygon[i]
                point2 = polygon[j]
                distance = self.dist(point1, point2)
                if distance >= max1:
                    max1 = distance
                    maxDiag1 = (point1, point2)
        return (maxDiag1, max1)
    
    #gets the mean of a series of coordinates
    def getMassCenter(self, region):
        mean_x = 0
        mean_y = 0
        for point in region:
            mean_x += point[0]
            mean_y += point[1]
        mean_x = mean_x/len(region)
        mean_y = mean_y/len(region)
        return (mean_x, mean_y)
    
    #crops the image so that the points in the given region are all shown
    def regionCropper(self, region, image):
        region.sort(key=lambda point : point[1])
        y_min = region[0][1]
        y_max = region[len(region)-1][1]
        region.sort(key=lambda point : point[0])
        x_min = region[0][0]
        x_max = region[len(region)-1][0]
        croppedImage = Image.new("RGB", (x_max-x_min + 1, y_max-y_min + 1))
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max+1):
                croppedImage.putpixel((x-x_min,y-y_min), image.getpixel((x,y)))
        return croppedImage
    
    #find if the object is a square
    def isSquare(self, region, hull):
        diag, dist = self.findBiggestDiagonal(hull)
        #find the ratio between diagonal and area : for a square, diag^2 should be equal to area*2
        diagAreaRatio = float(len(region)*2) / float(dist)
        if diagAreaRatio > 0.8 and diagAreaRatio < 1.4:
            return True
        else:
            return False
    
        #finds blue squares on an image and returns the squares as lists of points (their convex hull) and
    #their distance from the center
    def findSquares(self,image, color):
        print("--------------------------------binarizing the image")
        result = self.ColorBinarizator(image, color)
        
        
        width, height = result.size
            
        #find the regions
        #print("finding regions")
        regions = self.regionFinder(result)
        if len(regions) > 0:
            print("size of the region : " + str(len(regions[0])))
        
        #try to find squares
        '''
        squares = []
        dists = []
        print("classifying " + str(len(regions)) + " regions")
        for region in regions:
            #get the mass Center of the region
            massCenter = self.getMassCenter(region)
            #find the convex hull of the region
            hull = self.findConvexHull(region, height+1)
            #testing if the region is a square
            isThisSquare = self.isSquare(region, hull)
            #drawing squares
            if isThisSquare:
                squares.append(region)
                dists.append(massCenter[0] - (width/2))
        return (squares, dists)
        '''
        dists = []
        for region in regions:
            massCenter = self.getMassCenter(region)
            dists.append(massCenter[0] - width/2)
        return (regions, dists)
    
    #bynarizes the image according to fix threshold values on the colors
    def ColorBinarizator(self, image, color):
        image = image.filter(ImageFilter.BLUR)
        red, green, blue = image.split()
        width, height = image.size
        
        if color == "blue":
            impColor = blue
        elif color == "red":
            impColor = red
        else:
            impColor = green
        max = 0
        img = Image.new("L", (width, height))
        for x in range(width):
            for y in range(height):
                sum = blue.getpixel((x,y)) + green.getpixel((x,y)) + red.getpixel((x,y))+1
                value = round((float(impColor.getpixel((x,y))) / float(sum)) * 255)
                img.putpixel((x, y), value)
                if value > max:
                    max = value
                    
        img.save("beforeT.png")
        print "max " + color + " = " + str(max)
        if max > 120:
            threshold = round(0.85*float(max))
        else:
            threshold = 256
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(255)
                
        img = img.point(table)
                
        img = self.erode(img)
        img = self.dilate(img)
        
        img.save("afterT.png")
        
        return img
    
    def erode(self, image):
        paddedImage = self.createPaddedImage(image, 1)
        thresholdImg = paddedImage.point(lambda i, v=128: i > v and 255)
        filteredImg = thresholdImg.filter(ImageFilter.FIND_EDGES)
        thresholdImg = filteredImg.point(lambda i, v=128: i > v and 255)
        arithImg = ImageChops.subtract(paddedImage, thresholdImg)
        box = (1, 1, arithImg.size[0]-1, arithImg.size[1]-1)
        outImage = arithImg.crop(box)
        return outImage
    
    def dilate(self, image):
        paddedImage = self.createPaddedImage(image, 1)
        thresholdImg = paddedImage.point(lambda i, v=128: i > v and 255)
        thresholdImg = ImageChops.invert(thresholdImg)
        filteredImg = thresholdImg.filter(ImageFilter.FIND_EDGES)
        thresholdImg = filteredImg.point(lambda i, v=128: i > v and 255)
        arithImg = ImageChops.add(paddedImage, thresholdImg)
        box = (1, 1, arithImg.size[0]-1, arithImg.size[1]-1)
        outImage = arithImg.crop(box)
        return outImage
    
    
    def createPaddedImage(self, img, pad):
        '''Create an padded image - since it is created with resize() the bor=
    der =20
           pixels will be same (almost) as the original edge pixels.'''
        sizeX, sizeY = img.size
        paddedImage = img.resize((sizeX+2*pad, sizeY+2*pad))
        # paste original image into the new big image with an offset
        paddedImage.paste(img, (pad, pad))
        return paddedImage
    
    def equalize(self, h):
    
        lut = []
    
        for b in range(0, len(h), 256):
    
            # step size
            step = reduce(operator.add, h[b:b+256]) / 255
    
            # create equalization lookup table
            n = 0
            for i in range(256):
                lut.append(n / step)
                n = n + h[i+b]
    
        return lut