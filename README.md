# Proyek Analisis Data: E-Commerce Public Dataset

## Deskripsi Proyek
Proyek ini menganalisis dataset transaksi e-commerce untuk menjawab beberapa pertanyaan bisnis, seperti:
- Apa kategori produk yang paling banyak dan paling sedikit terjual?
- Di wilayah mana saja yang memiliki jumlah penjualan yang paling banyak?
- Bagaimana sebaran metode pembayaran yang digunakan?

## Tautan Penting
Dashboard Streamlit: [Link Streamlit](https://zt692dma8czfhprcp9yrlz.streamlit.app/)
Google Colab Notebook: [Link Colab](https://colab.research.google.com/drive/14RFjeLylrd32jCtFmFEXUB_0bnCHVicn?usp=sharing)
Repository GitHub: [GitHub Repo](https://github.com/rezaalra/dicoding-proyek-analisis-data/)

Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

## Run steamlit app
```bash
streamlit run dashboard/dashboard.py
