import cv2

    
def match_template(img,tmp,blur=0):  
    im = img
    if len(im.shape)==3:
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    if len(tmp.shape)==3:
        tmp=cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
    
    if blur > 0:
        kernel = (blur, blur) 
            
        im = cv2.blur(im, kernel)
        tmp = cv2.blur(tmp, kernel)
        
    h, w = tmp.shape[:2]     
    res = cv2.matchTemplate(im,tmp,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    x1,y1 = max_loc            
    x2,y2 = ( x1+w , y1+h )
    return img[y1:y1+h,x1:x1+w],x1,y1,x2,y2     