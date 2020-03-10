import xml.dom.minidom as minidom
 
def main():
    # gunakan fungsi parse() untuk me-load xml ke memori
    # dan melakukan parsing
    doc = minidom.parse("kasus.xml")
 
    # Cetak isi doc dan tag pertamanya
    print (doc.nodeName)
    print (doc.firstChild.tagName)
 
    nama = doc.getElementsByTagName("nama")[0].firstChild.data
    jenisKelamin = doc.getElementsByTagName("jenisKelamin")[0].firstChild.data
    alamat = doc.getElementsByTagName("alamat")[0].firstChild.data
    ponsel = doc.getElementsByTagName("ponsel")[0].firstChild.data
    surel = doc.getElementsByTagName("surel")[0].firstChild.data
    list_hobi = doc.getElementsByTagName("hobi")
 
    print ("Nama: {}\nJenisKelamin: {}\nAlamat: {}\nPonsel: {}\nSurel: {}".format(nama, jenisKelamin, alamat, ponsel, surel))
 
    print ("Memiliki {} hobi:".format(len(list_hobi)))
 
    for hobi in list_hobi:
        print ("-", hobi.getAttribute("name"))
 
 
if __name__ == "__main__":
    main()