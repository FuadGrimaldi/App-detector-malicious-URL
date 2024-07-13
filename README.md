# App-detector-malicious-URL

Web untuk mendeteksi URL berbahaya, web ini di dedikasikan untuk pengajuan HKI dalam rangka peningkatan akreditasi pada PT Institut Teknologi Nasional Bandung.

Website dibangun dengan framework flask pada server-side dan pada client-side dibangung menggunakan html dan framework css (tailwind). Model machine learning hasil training sudah tersedia di folder `ML`. Model ini di-import dan digunakan di bagian server-side untuk melakukan deteksi URL berbahaya. Anda dapat menemukan kode terkait pengolahan model di `app.py`.

## Prasyarat

Sebelum melanjutkan, pastikan Anda telah memenuhi persyaratan berikut pada mesin Anda.

- Python version > 3
- git
- pip
- text editor -> Visual Studio Code for me
- Model ML
  _note: model hasil training sudah tersedia di folder ML_

## Cara install di local

- Clone repository ini

```bash
$ git clone https://github.com/FuadGrimaldi/App-detector-malicious-URL.git
```

- Ubah direktori ke folder tempat Anda ingin meletakkan kode

```bash
$ cd App-detector-malicious-URL
```

- buat python virtual environment pada folder tersebut kemudian aktifkan

```bash
$ python -m venv myenv
$ source myenv/bin/activate  # Untuk Unix/MacOS
$ source myenv/Scripts/activate  # Untuk windows git bash
```

- install depedencies pada requirement.txt

```bash
$ pip install -r requirements.txt
```

- Jalankan server pengembangan di mesin Anda

```bash
$ flask --app app run --debug
```

- Kunjungi aplikasi melalui [localhost:5000](localhost:5000)

## Package utama

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Tailwind](https://tailwindcss.com/)
- [sklearn](https://scikit-learn.org/stable/)

## opsi

- nonaktifkan virtual environment

```bash
$ deactivate
```

- nonaktifkan server (ctrl + c)

```bash
$ ^C
```

### Dengan perubahan ini, dokumentasi akan lebih mudah diikuti dan memberikan panduan yang lebih jelas bagi pengguna.
