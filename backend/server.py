from flask import Flask
from flask import request, make_response, jsonify
import os
from createSummary import createSummary
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)  # これで全てのルートでCORSが有効

@app.route('/api/upload', methods=['POST'])
@cross_origin(supports_credentials=True) 
def upload_file():
    print("バックエンドきた！！！")
    if 'image' not in request.files:
        return {"error": "No image provided."}, 400

    image = request.files['image']
    if image.filename == '':
        return {"error": "No image provided."}, 400

    # 保存先ディレクトリの設定
    save_dir = 'uploaded_images'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        

    # 画像をサーバーに保存
    image.save(os.path.join(save_dir, image.filename))
    # 保存されているか確認用    
    res = createSummary(image.filename)
    response = {'result': res}
    return make_response(jsonify(response))

    # return {"message": "Image uploaded and saved."}

if __name__ == "__main__":
    app.debug = True
    # app.run()
    app.run(host='10.232.20.8', port=8080)
