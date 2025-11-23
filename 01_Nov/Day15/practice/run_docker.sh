#!/bin/bash

IMAGE_NAME="myapp:latest"

echo "[INFO] Building docker image..."
docker build -t $IMAGE_NAME .
if [ $? -ne 0 ]; then
	echo "[ERROR] Build failed!"
	exit 1
fi

echo "[INFO] Running container...."
CID=$(docker run -d $IMAGE_NAME)
if [ $? -ne 0 ]; then
	echo "[ERROR] Failed to run container!"
	exit 1
fi

echo "[INFO] container ID: $CID"

echo "[INFO] Logs:"
docker logs $CID

echo "[INFO] stopping container..."
docker stop $CID >/dev/null

echo "[INFO] removing container..."
docker rm $CID >/dev/null

echo "[SUCCESS] Build + Run completed!"


