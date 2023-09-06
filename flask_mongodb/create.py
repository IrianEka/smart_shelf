from flask import Flask, request, jsonify
import pymongo


app = Flask(__name__)

password = "SGzkyaxsykdPzYYf"
uri = f"mongodb+srv://irianeka21:{password}@jayamahe.nnvynod.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client['test']
my_collection = db['test_collection']

@app.route('/tambah_data', methods=['POST'])
def tambah_data():
    data = request.json  # Mengambil data dari request dalam format JSON

    # Masukkan data ke MongoDB
    result = my_collection.insert_one(data)

    if result.inserted_id:
        return jsonify({'message': 'Data berhasil ditambahkan', 'data_id': str(result.inserted_id)})
    else:
        return jsonify({'message': 'Gagal menambahkan data'}), 500


if __name__ == '__main__':
    app.run(host='192.168.0.103', port=5001)
