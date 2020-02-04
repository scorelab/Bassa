## Setup Minio server

*Make sure you have docker already installed in your system.*

We will be creating minio server with persistent storage, so we need to map local persistent directories from the host OS to virtual config `~/.minio` and export `/data` directories. And we are also overwriting the access and secret keys.

**GNU/Linux and macOS**

`sudo docker run -p 9000:9000 --name minio \
  -e "MINIO_ACCESS_KEY=bassa" \
  -e "MINIO_SECRET_KEY=bassa123" \
  -v /mnt/data:/data \
  minio/minio server /data`

**Windows** (*Run cli in administrator mode*)

`docker run -p 9000:9000 --name minio \
  -e "MINIO_ACCESS_KEY=bassa" \
  -e "MINIO_SECRET_KEY=bassa123" \
  -v D:\data:/data \
  minio/minio server /data
`
