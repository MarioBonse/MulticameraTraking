import camera as cam
import HSVObjTracking as HSVTr
import 3dplot

def main():
    camera1 = cam.camera(1, "/dev/video0")
    camera2 = cam.camera(2, "/dev/video3")
    #red ball
    ballLower = (137, 88, 55)
    ballUpper = (183, 255, 255)
    if camera1.createCameraMatrixUndistort() == False:
        return False
    if camera2.createCameraMatrixUndistort() == False:
        return False
    camera1.showvideo()
    camera2.showvideo()
    trackingObject = HSVtr.HSVObjTracking(ballLower, ballUpper, camera1, camera2)
    x,y,z = trackingObject.threedMovementsRecontstruction()
    3dplot.displayanimation(x, y, z)

if __name__ == "__main__":
    main()

###yellow ball
#ballLower = (14, 67, 34)
#ballUpper = (57, 255, 255)
#
######red ball
#ballLower = (137, 88, 55)
#ballUpper = (183, 255, 255)
