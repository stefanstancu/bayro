import sys
import cv2

def test_patterns():
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

def convert_image(img_name):
    img_in = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    img_out = cv2.cvtColor(img_in, cv2.COLOR_BayerBG2BGR)

    img_out_name = img_name.split('.')[0]
    cv2.imwrite(img_out_name + '.jpg', img_out)

def convert(img_list):
    for img in img_list:
        convert_image(img)

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Error, please specify a file or ptest. Use --help for more options.")
        exit()

    elif sys.argv[1] == 'ptest':
        test_patterns()

    elif sys.argv[1] == '--help':
        print("Commands:\n    ptest\n    convert [IMAGES]\n")

    elif sys.argv[1] == 'convert':
        convert(sys.argv[2:])
    
