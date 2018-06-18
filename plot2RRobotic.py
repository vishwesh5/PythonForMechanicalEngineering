# -*- coding: utf-8 -*-
"""
Simulate 2R Robotic arm

Created on Mon Jun 18 09:56:21 2018

@author: vshrima
"""
import matplotlib.pyplot as plt
from math import pi, cos, sin
from numpy import linspace
from os import mkdir
# x0 = 0, y0 = 0
# l1 = 1
# l2 = 0.5

folderName = 'robotic2RPlots/'
try:
    os.mkdir(folderName)
except:
    print("%s exists. Continuing..."%(folderName))
def plotRoboticArmPosition(x0,y0,x1,y1,x2,y2,theta1,theta2,imgCount):
    # Clear figure
    plt.clf()
    plt.cla()
    plt.close()
    plt.plot(x0,y0,'o',markersize=10)
    plt.plot(x1,y1,'o',markersize=10)
    plt.plot(x2,y2,'o',markersize=10)
    # Plot link 1
    plt.plot([x0,x1],[y0,y1],'-',c='k',label='Link 1')
    # Plot link 2
    plt.plot([x1,x2],[y1,y2],'-',c='r', label = 'Link 2')
    # Turn axis off
    title = "2R Robotic arm for theta1 = {:.2f}, theta2 = {:.2f}".format(theta1,theta2)
    plt.title(title)
    plt.legend(loc='upper left')

def main():
    # Define lengths
    l1 = 1
    l2 = 0.5
    # Base of robot
    x0 = 0
    y0 = 0

    # Number of theta values
    n_theta = 100
    
    theta1 = linspace(-pi/2,pi/2,n_theta)
    theta2 = linspace(-pi/2,pi/2,n_theta)
    
    imgCount = 0
    
    for i in theta1:
        for j in theta2:
            # Link1 - link2 connector
            x1 = x0+l1*cos(i)
            y1 = x0+l1*sin(i)
            # Link 2 end
            x2 = x1 + l2*cos(j)
            y2 = y1 + l2*sin(j)
            # Plot position
            plotRoboticArmPosition(x0,y0,x1,y1,x2,y2,i,j,imgCount)
            plt.xlim([-(l1+l2)*1.1,(l1+l2)*1.1])
            plt.ylim([-(l1+l2)*1.1,(l1+l2)*1.1])
            fileName = folderName+'plot_{0:06d}.png'.format(imgCount)
            plt.savefig(fileName)
            imgCount+=1
        theta2 = theta2[::-1]

if __name__ == "__main__":
    main()