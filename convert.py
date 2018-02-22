import sys
import cv2

def test_patterns(opencl=False):
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

def convert_image(img_name, opencl=False):
    
    img_in = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

    if opencl:
        img_in = cv2.UMat(img_in)

    img_out = cv2.cvtColor(img_in, cv2.COLOR_BayerBG2BGR)

    img_out_name = img_name.split('.')[0]
    cv2.imwrite(img_out_name + '.jpg', img_out)

def convert(img_list, opencl=False):
    for img in img_list:
        print("Converting " + img)
        convert_image(img, opencl)

if __name__ == '__main__':

    opencl = False
    if "-O" in sys.argv:
        opencl = cv2.ocl.haveOpenCL()
        print("OpenCL available: " + str(opencl))
        cv2.ocl.setUseOpenCL(opencl)
        sys.argv.remove("-O")

    if len(sys.argv) == 1:
        print("Error, please specify a file or ptest. Use --help for more options.")
        exit()

    elif sys.argv[1] == 'ptest':
        test_patterns(opencl)

    elif sys.argv[1] == '--help':
        print("Commands:\n    --help\n    ptest\n    convert [IMAGES]\n Options:\n    -O    Use OpenCL Bindings")

    elif sys.argv[1] == 'convert':
        convert(sys.argv[2:], opencl)

    else:
        print("Error: No command given. Use --help for available commands")
    
