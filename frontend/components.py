import streamlit as st


def render_hero():
    st.markdown("# 🎓 E-Complaint Smart Campus")
    st.markdown(
        "Sistem berbasis Natural Language Processing untuk membantu mahasiswa "
        "mengirimkan keluhan dan mendapatkan rekomendasi unit penanganan "
        "secara cepat, rapi, dan terarah."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("💬 Klasifikasi Keluhan")

    with col2:
        st.info("⚡ Prediksi Prioritas")

    with col3:
        st.info("🏢 Rekomendasi Unit")

    with col4:
        st.info("🏫 Smart Campus")


def section_title(title, description):
    st.markdown(f"## {title}")
    st.markdown(description)


def input_helper():
    st.info(
        "Klik kolom input di bawah ini, lalu tuliskan keluhan secara singkat dan jelas. "
        "Contoh: WiFi di gedung B sering mati saat kelas online."
    )


def render_result(result):
    st.markdown("## Hasil Prediksi")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown(f"### {result['category_icon']}")
            st.markdown("Kategori Keluhan")
            st.markdown(f"## {result['kategori']}")

    with col2:
        with st.container(border=True):
            st.markdown(f"### {result['priority_icon']}")
            st.markdown("Tingkat Prioritas")
            st.markdown(f"## {result['prioritas']}")

    with col3:
        with st.container(border=True):
            st.markdown("### 🏢")
            st.markdown("Unit Penanganan")
            st.markdown(f"## {result['unit']}")

    st.success(f"Keterangan prioritas: {result['priority_info']}")

    st.markdown("### Ringkasan")
    st.write(
        f"Keluhan tersebut masuk kategori {result['kategori']} "
        f"dengan prioritas {result['prioritas']}. "
        f"Sistem merekomendasikan laporan diteruskan ke {result['unit']}."
    )


def render_flow():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.markdown("### 💬")
            st.markdown("### Input Keluhan")
            st.write("Mahasiswa menuliskan keluhan melalui kolom input aplikasi.")

    with col2:
        with st.container(border=True):
            st.markdown("### 🧹")
            st.markdown("### Preprocessing")
            st.write("Sistem membersihkan teks agar siap diproses oleh model.")

    with col3:
        with st.container(border=True):
            st.markdown("### 🤖")
            st.markdown("### Prediksi Model")
            st.write("Model memprediksi kategori dan tingkat prioritas keluhan.")

    with col4:
        with st.container(border=True):
            st.markdown("### 🏢")
            st.markdown("### Unit Penanganan")
            st.write("Sistem menampilkan rekomendasi unit layanan kampus.")


def render_unit_mapping():
    st.markdown("## Rekomendasi Unit Penanganan")

    data = {
        "Kategori": [
            "Akademik",
            "Administrasi",
            "Keuangan",
            "Jaringan",
            "Fasilitas",
            "Kebersihan",
            "Keamanan",
        ],
        "Unit Penanganan": [
            "Program Studi / Jurusan",
            "BAAK / Administrasi Fakultas",
            "BPPK / Bagian Keuangan",
            "UPT TIK / Tim Jaringan",
            "Sarana dan Prasarana",
            "Sarana dan Prasarana",
            "Satpam / Unit Keamanan Kampus",
        ],
    }

    st.table(data)


def render_about():
    st.markdown("## E-Complaint Smart Campus")

    st.write(
        "E-Complaint Smart Campus merupakan aplikasi untuk membantu pengelolaan "
        "keluhan mahasiswa secara lebih terarah. Sistem ini memanfaatkan Natural "
        "Language Processing dan model Machine Learning untuk mengklasifikasikan "
        "keluhan, menentukan tingkat prioritas, serta memberikan rekomendasi unit "
        "penanganan."
    )

    st.markdown("### Peran Software Engineering")

    st.write(
        "Bagian Software Engineering berfokus pada implementasi model ke dalam "
        "aplikasi web, perancangan antarmuka, integrasi model, serta deployment "
        "agar sistem dapat diakses secara online."
    )

    st.markdown("### Kelompok 10")

    anggota = {
        "No": [1, 2, 3, 4, 5, 6],
        "Nama": [
            "La Ode Alifatur Yakin",
            "Zacky Fiqran Kasmada",
            "Andi Nanis Sacharina",
            "Riby Sesharia Ramba",
            "Melani Cicelia Saputri Lapake",
            "Alifah Lauthfiyah Nurwasilah",
        ],
        "NIM": [
            "F1G124___",
            "F1G124___",
            "F1G123018",
            "F1G123013",
            "F1G124___",
            "F1G124___",
        ],
    }

    st.table(anggota)


def render_footer():
    st.divider()
    st.caption("🎓 E-Complaint Smart Campus · Kelompok 10 · NLP dan Machine Learning")