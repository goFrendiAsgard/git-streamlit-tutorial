# Apa Ini

Sebuah repository untuk mengenalkan git dan streamlit pada tokoh fiksi `Faizah` dan `Rizki`, dua orang data analyst di kantor desa Sukamaju.

# Clone Project

Perintah berikut akan meng-clone repository ini ke komputer `Faizah` dan `Rizki`:

```bash
git clone git@github.com:goFrendiAsgard/git-streamlit-tutorial.git
```

# Melakukan Setup

Supaya tidak menjalankan banyak perintah berkali-kali, maka data engineer di tempat `Faizah` dan `Rizki` sudah mempersiapkan seubah script `setup.py`.

Untuk menjalankan `setup.py`, maka `Faizah` dan `Rizki` perlu menjalankan:

```bash
source ./setup.sh
```

Perintah di atas akan:

- Membuat folder `venv` jika belum ada. Folder `venv` akan berisi python virtual environment untuk repository ini
- Mengaktifkan python virtual environment di folder `venv`
- Menginstall `streamlit` dan `plotly` ke dalam python virtual environment
- Menyampaikan kata sambutan dari Bapak Kepala Desa Sukamaju.

# Menjalankan Aplikasi Streamlit

Untuk menjalankan aplikasi streamlit, maka `Faizah` dan `Rizki` perlu menjalankan perintah berikut:

```bash
streamlit run main.py
# Jika Faizah dan Rizki menggunakan Windows dan WSL, maka sebaiknya menjalankan perintah
# streamlit run main.py --server.headless true
```

Hasilnya kurang lebih begini:

![](images/Asia%20GDP.png)

# Kode Streamlit

Kode yang kita punya relatif sederhana

```python
import streamlit as st
import plotly.express as px

# Load Asia's GDP
df = px.data.gapminder().query("continent=='Asia'")

st.title('Asia GDP from 1952-2007')
st.table(df)
```

Pertama kita perlu mengimport library `streamlit` dan `plotly.express`. Berdasarkan kabar terbaru, mengimport Python package masih belum dikenakan bea cukai, jadi kita bisa mengimport semua package yang kita butuhkan secara gratis.

Silahkan menjelajahi [pypi.org](http://pypi.org) untuk mencari package yang diperlukan.

Setelah melakukan import, langkah berikutnya adalah mengambil data GDP negara Asia. Data ini merupakan data bawaan dari package plotly yang diperoleh secara legal, tidak melalui ransomware. Adapun data yang kita dapatkan akan berbentuk pandas dataframe.

Terakhir, kita menampilkan komponen-komponen yang kita perlukan.

- `st.title` akan menampilkan judul
- `st.table` akan menampilkan data frame dalam bentuk tabel.

# Tugas dari Pak Kades

Tak seperti kebanyakan boomer pada umumnya, Pak Kades Sukamaju sangat akrab dengan teknologi, AI, blockchain, web3, dan anime. Pak Kades bahkan mengikuti penayangan `Kimetsu no Yaiba`, dan kerap mengadakan acara nobar di balai desa.

Pak Kades merasa perlu untuk mengetahui data-data GDP negara tetangga, tapi dia tidak ingin mendapatkan informasi yang terlalu banyak.

Menurut Pak Kades, ada 2 hal yang perlu dilakukan di sini:

- Menambahkan filter berdasarkan benua, supaya data yang ditampilkan tidak terlalu banyak.
- Menampilkan data dalam bentuk line chart, supaya komparasi beberapa negara bisa dibaca dengan lebih mudah.

Pak Kades mempercayakan tanggung jawab besar ini pada dua anak muda Gen-z yang sangat berbakat, `Faizah` dan `Rizki`.

Pak Kades juga menyuruh `Faizah` dan `Rizki` untuk membuka [dokumentasi streamlit](https://docs.streamlit.io/library/api-reference). Ia yakin, literasi kedua anak muda itu akan bisa membuka cakrawala masa depan Desa Sukamaju.

## Filter Faizah

Faizah mengawali pekerjaannya dengan mengucap Bismillah, dan membuat sebuah branch baru:

```bash
git checkout -b feat/per-continent-filter
```

Tak butuh lama bagi Faizah untuk menyelesaikan tugas Pak Kades. Dengan cekatan, Faizah memodifikasi `main.py` menjadi seperti berikut:

```python
import streamlit as st
import plotly.express as px

continent = st.selectbox(label='Benua', options=['Asia', 'Africa', 'Americas', 'Europe', 'Oceania'])

# Load Asia's GDP
df = px.data.gapminder().query(f"continent=='{continent}'")

st.title(f'{continent} GDP from 1952-2007')
st.table(df)
```

Untuk menguji apakah pekerjaannya sudah berjalan dengan baik, maka me-refresh browser nya, dan mendapatkan tampilan seperti ini.

![](images/Asia%20GDP%20filtered.png)

Faizah melakukan scroll ke bawah dan memastikan ada Indonesia di benua Asia. Lalu Faizah berseru "Wah, ada Indonesia".

Setelah puas dengan hasil pekerjaannya, Faizah melakukan push ke github

```bash
git add . -A
git commit -m 'Menambah filter'
git push -u origin feat/per-continent-filter
```

Faizah lantas membuat sebuah pull request di github dan meminta review/approval dari Pak Kades.

# Visualisasi Rizki

Di saat yang sama, Rizki juga mengerjakan tugas Pak Kades dengan penuh amanah.

Seperti Faizah, Rizki memulai tugasnya dengan membuat sebuah branch

```bash
git checkout -b feat/line-chart-visualization
```

Sembari menyesap secangkir kopi hitam yang lebih pahit dari kehidupan, Rizki mengertakkan kedua tangannya. Jari-jarinya menari anggun di atas keyboard, menuangkan imajinasinya dalam barisan kode nan elegan.

```python
import streamlit as st
import plotly.express as px

# Load Asia's GDP
df = px.data.gapminder().query("continent=='Asia'")

st.title('Asia GDP from 1952-2007')
st.plotly_chart(px.line(
    data_frame=df, x='year', y='gdpPercap', color='country'
))

st.title('Asia GDP from 1952-2007')
st.table(df)
```

Rizki menatap layar monitor dengan sedih, ternyata GDP Indonesia rendah sekali. Pantas saja, gajinya bulan ini belum cair.

![](images/Asia%20GDP%20line-chart.png)

Tapi Rizki yakin, di tangan pemuda-pemuda berbakat sepertinya, nasib Indonesia akan lebih baik. Rizki kemudian melakukan push ke github dan membuat sebuah pull request.

```bash
git add . -A
git commit -m 'Visualisasi line chart'
git push -u origin feat/line-chart-visualization
```

# Code Review

Pak Kades terharu melihat pekerjaan Faizah dan Rizki yang sangat baik. Benar-benar sesuai dengan butir-butir Pancasila dan wawasan kebangsaan.

Dengan tersenyum, Pak Kades memberikan komentar `LGTM`, melakukan approval, dan melakukan merge ke branch `main`.

Kini kode di branch main tampak seperti berikut:

```python
import streamlit as st
import plotly.express as px

continent = st.selectbox(label='Benua', options=['Asia', 'Africa', 'Americas', 'Europe', 'Oceania'])

# Load Asia's GDP
df = px.data.gapminder().query(f"continent=='{continent}'")

st.title('Asia GDP from 1952-2007')
st.plotly_chart(px.line(
    data_frame=df, x='year', y='gdpPercap', color='country'
))

st.title(f'{continent} GDP from 1952-2007')
st.table(df)
```

Sebuah pengejawantahan sikap gotong royong yang terlihat nyata. Pekerjaan Faizah dan Rizki saling melengkapi satu sama lain. Indahnya kolaborasi dan pluralisme!

# Mengubah Caption

Rizki dan Faizah masing-masing melakukan pull ke branch main di komputer lokal masing-masing.

Rizki meras ada yang kurang oke dengan caption yang ia buat. Bukankah dashboard desa Sukamaju ini bersifat global? Tidak hanya regional di skala Asia? Maka Rizki membuat sebuah branch dan pull request untuk memperbaiki caption yang ia buat:

```bash
git checkout -b fix/line-chart-caption
```

Sama seperti sebelumnya, Rizki melakukan modifikasi kodenya

```python
import streamlit as st
import plotly.express as px

continent = st.selectbox(label='Benua', options=['Asia', 'Africa', 'Americas', 'Europe', 'Oceania'])

# Load Asia's GDP
df = px.data.gapminder().query(f"continent=='{continent}'")

st.title(f'{continent} GDP from 1952-2007')
st.plotly_chart(px.line(
    data_frame=df, x='year', y='gdpPercap', color='country'
))

st.title(f'{continent} GDP from 1952-2007')
st.table(df)
```

Rizki lantas membuat PR dan meminta Pak Kades yang tengah tidur siang untuk melakukan review/merge.

Pak Kades lantas meminta Rizki dan Faizah untuk melakukan pull di branch main.

```bash
git checkout main
git pull origin main
```

# Awal Mula Sebuah Konflik

Puas dengan pekerjaannya, Rizki membuat sebuah PR lain, untuk memeriahkan dashboard. Nama branch yang dia buat adalah `feat/rizki-celebration` dan membuat pull request.

```python
import streamlit as st
import plotly.express as px

continent = st.selectbox(label='Benua', options=['Asia', 'Africa', 'Americas', 'Europe', 'Oceania'])

# Load Asia's GDP
df = px.data.gapminder().query(f"continent=='{continent}'")

st.title(f'{continent} GDP from 1952-2007')
st.plotly_chart(px.line(
    data_frame=df, x='year', y='gdpPercap', color='country'
))

st.title(f'{continent} GDP from 1952-2007')
st.table(df)
st.balloons()
```

Di saat yang sama, Faizah ternyata memiliki inisiatif yang sama. Namun berbeda dari Rizki, Faizah tahu bahwa streamlit sudah diakuisi snowflake, sehingga ia memutuskan untuk menggunakan `st.snow()`, bukan `st.balloons()`.

Faizah membuat sebuah branch `feat/faizah-celebration` dan membuat pull request.


```python
import streamlit as st
import plotly.express as px

continent = st.selectbox(label='Benua', options=['Asia', 'Africa', 'Americas', 'Europe', 'Oceania'])

# Load Asia's GDP
df = px.data.gapminder().query(f"continent=='{continent}'")

st.title(f'{continent} GDP from 1952-2007')
st.plotly_chart(px.line(
    data_frame=df, x='year', y='gdpPercap', color='country'
))

st.title(f'{continent} GDP from 1952-2007')
st.table(df)
st.snow()
```

Pak Kades melakukan approval dan merge pada PR Rizki, dan sebuah hal yang tak didugapun terjadi. Muncul conflict, sehingga pull request Faizah tidak bisa di merge.

Bagaimanakah Faizah me resolve semua ini? Akankan pertemanannya dengan Rizki berakhir?

# Penyelesaian Konflik

Faizah tahu, bahwa konflik ini tidak sulit untuk diselesaikan. Faizah adalah seorang profesional yang sudah berkarya sejak masih dalam kandungan.

Maka Faizah berpindah ke branch main, melakukan merge ke branch nya sendiri, dan me-resolve konflik yang ada.

```bash
git checkout main
git pull origin main
git checkout feat/faizah-celebration
git merge main
```

Di VSCode Faizah, muncul beberapa opsi di area konflik, dan dengan bijaksana, ia memilih `Accept both Change`.

Faizah lantas meng-update PR nya.

```bash
git add . -A
git commit -m 'Menyelesaikan konflik'
git push -u origin feat/faizah-celebration
```

Pak Kades begitu bangga atas inisiatif Faizah. Ia pun melakukan review, memberikan approval, dan melakukan merge request.

Lagi-lagi Faizah dan Rizki melakukan pull di branch main.
