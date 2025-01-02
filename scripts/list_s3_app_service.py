import boto3
from flask import Flask, jsonify

list_s3_app = Flask(__name__)

aws_region = "AWS_REGION"
#aws_access_key_id = "AWS_ACCESS_KEY_ID"
#aws_secret_access_key = "AWS_SECRET_ACCESS_KEY"
s3_bucket_name = "BUCKET_NAME"

@list_s3_app.route('/list-bucket-content/<path:path>', methods=['GET'])
@list_s3_app.route('/list-bucket-content/', defaults={'path': ''}, methods=['GET'])

def list_objects(path):
    s3_client = boto3.client('s3', region_name=aws_region)    
    try:
        result = s3_client.list_objects_v2(Bucket=s3_bucket_name, Prefix=path)
        list_of_objects = []

        if 'Contents' not in result:
            return jsonify({"Message": "Given path doesn't have any Contents, Please retry!", "Path": path}), 404
        
        for object in result.get('Contents', []):
            print(object['Key'])
            list_of_objects.append(object['Key'])
            
        return jsonify({"Path": path, "List": list_of_objects}), 200
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__ == '__main__':
    list_s3_app.run(host='0.0.0.0', port=5000)
