from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from flask import current_app
import os

main = Blueprint("main", __name__)

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]
    )

@main.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "AI Resume Screener is running ✅"})

@main.route("/upload", methods=["POST"])
def upload_cv():
    if "cv" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["cv"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Only PDF and DOCX files are allowed"}), 400

    filename = secure_filename(file.filename)
    save_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    file.save(save_path)

    return jsonify({
        "message": "File uploaded successfully",
        "filename": filename,
        "path": save_path
    }), 200