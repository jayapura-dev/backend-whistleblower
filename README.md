<p align="center"><img src="https://live.staticflickr.com/65535/49873465473_ac1790f091_b.jpg" width="600px"></p>

<p align="center">
  <a href="https://gitter.im/jayapura_django/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge"><img src="https://badges.gitter.im/jayapura_django/community.svg" alt="Gitter" target="_blank"></a>
  <a href="https://github.com/jayapura-dev/backend-whistleblower/actions"><img src="https://github.com/jayapura-dev/backend-whistleblower/workflows/Production%20Server/badge.svg" alt="Build Status" target="_blank"></a>
  <a href="https://github.com/Ekhel/whistleblower/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT" target="_blank"></a>
</p>

## Tentang Whistleblower Sistem :
  - Whistle Blower Adalah Sistem Pengaduan Electronik yang dibuat khusus untuk Lembaga / Dinas
  yang menjalankan Fungsi pemeriksaan Keuangan aset dll.

  ----------------------------------------------------------------------------------------------------------------------

## System Requirements :
* Bahasa Utama :
  - Python

* Framework :
  - Django 3.0.0

* DBMS :
  - Postgre

* Library :
  - Django REST Framework (REST API)
  - Gunicorn (Web Server)
  - WhiteNoise (Static Files)
  - Django CORS-Header (Middleware Cors Origin for API)
  - ![requirements](https://github.com/jayapura-dev/backend-whistleblower/blob/master/requirements.txt)

* Frontend :
  - [Frontend Whistle](https://github.com/jayapura-dev/frontend-whistleblower)

* HOST
  - [Server VPS]()

----------------------------------------------------------------------------------------------------------------------
## Fitur Backend :
  - [x] Dashboard Administrator (default Django)
  - [x] Dashboard Administrator (Custom Setup)
  - [x] 2 Level Akses (Administrator & Pemeriksa)
  - [ ] CRUD Distrik & Kampung 
  - [x] Statistik Aduan
  - [x] CRUD Kategori
  - [x] Servis RESTFULL API (Pengaduan)
  - [x] Servis API (Distrik, Kampung, Kategori, CallBack url Pengaduan)
  - [ ] Menajemen User & Roles
  - [ ] Kirim Data Aduan Ke Pemeriksa
  - [ ] File Aduan

-----------------------------------------------------------------------------------------------------------------------

## Progres Pembuatan & Pengembangan :

* *Sabtu 9 Mei 2020*
  - Buat Project [Solved]
  - Buat App Pengadua [Solved]
  - Buat repository [Solved]

* *Minggu 10 Mei 2020*
  - Buat DB Postgre [Solved]
  - Buat Model Distrik & Kampung [Solved]
  - Buat Login Page [Solved]

* *Sabtu 5 Juni 2020*
  - Ganti Template [Solved]
  - Buat Authentikasi Login / Logout [Solved]

* *Sabtu 6 Juni 2020*
  - Buat Halaman Dashboard [Solved]
  - Buat Halaman Data Master [Solved]
  - Buat Halaman Distrik [Solved]
  - Buat Halaman Kampung [Solved]

* *Minggu 7 Juni 2020*
  - Buat Halaman Pengaduan [Solved]
  - Buat Halaman Detail Pengaduan [Solved]

* *Rabu 10 Juni 2020*
  - Buat Fungsi CRUD Halaman Kategori [Solved]

* *Kamis 11 Juni 2020*
  - Include rest_framework [Solved]
  - Setup Serializer Class [Solved]
  - Setup Generic Viewset API [Soveld]

* *Senin 15 Juni 2020*
  - Set Permission Class rest_framework [Solved]
  - Set corsheader CORS [Solved]
  - Setup ViewSet API Query Distrik dan Kampung [Solved]

* *Selasa 16 Juni 2020*
  - install django_filter untuk rest_framework [Solved]
  - Set filter backend ke Serializers Aduan [Solved]
  - Set default Filter menggunakan filter_backend [Solved]

* *Sabtu 20 Juni 2020*
  - Install Django Rest Knox [Solved]
  - Buat Register API Via Knox Token [Solved] Tested Frontend [Solved]
  - Buat Instance User [Solved]
  - Setup Response, Basic Authentikasi API dan Session Authentikasi API [Solved]

