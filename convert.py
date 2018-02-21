import cv2

def convert():
    img = cv2.imread("test.bmp", cv2.IMREAD_GRAYSCALE)

    img_out = {
        'BG2BGR': cv2.cvtColor(img, cv2.COLOR_BayerBG2BGR),
        'GB2BGR': cv2.cvtColor(img, cv2.COLOR_BayerGB2BGR),
        'RG2BGR': cv2.cvtColor(img, cv2.COLOR_BayerRG2BGR),
        'GR2BGR': cv2.cvtColor(img, cv2.COLOR_BayerGR2BGR),
        'BG2RGB': cv2.cvtColor(img, cv2.COLOR_BayerBG2RGB),
        'GB2RGB': cv2.cvtColor(img, cv2.COLOR_BayerGB2RGB),
        'RG2RGB': cv2.cvtColor(img, cv2.COLOR_BayerRG2RGB),
        'GR2RGB': cv2.cvtColor(img, cv2.COLOR_BayerGR2RGB)
    }
    
    for key, value in img_out.items():
        cv2.imwrite(key + '.jpg', value)

if __name__ == '__main__':
    convert()
