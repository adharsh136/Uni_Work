import boto3,argparse

#Constants
bucket = '23796349-lab9'
client = boto3.client('rekognition')

# Argument Parsing
parser = argparse.ArgumentParser(description='AWS_Rekognition_options')
parser.add_argument('--labelrecog', '-l', action='store_true', help='Label Recognition')
parser.add_argument('--imgmoderation', '-i', action='store_true', help='Image Moderation')
parser.add_argument('--faceanalyse', '-f', action='store_true', help='Facial Analysis')
parser.add_argument('--exttxt', '-e', action='store_true', help='Extract Text')
parser.add_argument('--photo', '-p', required=True, help='Photo name with extension present in your S3 bucket')
args = parser.parse_args()

#Label Recognition
def detectLabels(photo_name):
    reponse = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo_name}})
    print("Detection")
    print("---------")
    for label in reponse['Labels']:
        print(f"Label: {label['Name']} | Confidence: {int(label['Confidence'])}%")

#Image Moderation
def imgMod(photo_name):
    reponse = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo_name}})
    print("Detection")
    print("---------")
    for label in reponse['ModerationLabels']:
        print(f"Label: {label['Name']} | Confidence: {int(label['Confidence'])}%")

#Facial Analysis
def analyFace(photo_name):
    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo_name}}, Attributes=['ALL'])
    faceCount = 0
    for face in response['FaceDetails']:
        faceCount+=1
        print("Face Number: "+ str(faceCount))
        print("Detection")
        print("---------")
        print("Gender: "+face['Gender']['Value']+" | Confidence: "+str(int(face['Gender']['Confidence']))+"%")
        print("Age Range (years): "+str(face['AgeRange']['Low'])+" to "+str(face['AgeRange']['High']))
        print("Glasses: "+str(face['Eyeglasses']['Value'])+" | Confidence: "+str(int(face['Eyeglasses']['Confidence']))+"%")
        print("------------------------------------------------------------------------------")

#Extract Text
def extText(photo_name):
    response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo_name}})
    print("Detection")
    print("---------")
    for text in response['TextDetections']:
        print(f"Text detected: {text['DetectedText']} | Confidence: {int(text['Confidence'])}%")

#Calling appropriate function based on the option specified
if args.labelrecog:
    detectLabels(args.photo)

if args.imgmoderation:
    imgMod(args.photo)

if args.faceanalyse:
    analyFace(args.photo)

if args.exttxt:
    extText(args.photo)

