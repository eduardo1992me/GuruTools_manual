from django.test import TestCase
import time
from datetime import timedelta, date

posicion = 0
currency = ""

target_url= "httdsfdsfsfop_cur=MXN&userIntent=&selectedRoomType=218763984&selectedRatePlan=278240039&searchId=5c79f714-5515-42d7-b3bd-de08eb3e1516"


if currency == "MXN":
    remove_cr = "MXN$"
    for a in range (len(list_price)):
        price_raw = list_price[a]
        clear_price = price_raw.replace(remove_cr, '')
        list_price[a] = clear_price


def url_convert(url, cycle):
    posicion = 0
    encontrado = False
    encontrado_fin_url = False
    for i in url:
        if i == "?" and cycle == 0:
            date_chkin = date.today() + timedelta(days=1)
            date_chout = date.today() + timedelta(days=2)
            old_chkin = ""
            old_chout = ""

            for ch in url_out:
                #print(ch, url_out[posicion], posicion)
                #print(url_out[posicion+1:posicion+6])
                if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
                    old_chkin = url_out[posicion+7:posicion+17]
                    old_chout = url_out[posicion+25:posicion+35]
                    url_out = url_out.replace(old_chkin, str(date_chkin))
                    url_out = url_out.replace(old_chout, str(date_chout))
                    print(url_out)
            posicion += 1
           # print(f"Fecha en ciclo 0 es:: {date_chkin}")
        elif i == "?" and cycle == 1:
            date_chkin = date.today() + timedelta(days=7)
            date_chout = date.today() + timedelta(days=8)
            old_chkin = ""
            old_chout = ""

            for ch in url_out:
                #print(ch, url_out[posicion], posicion)
                #print(url_out[posicion+1:posicion+6])
                if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
                    old_chkin = url_out[posicion+7:posicion+17]
                    old_chout = url_out[posicion+25:posicion+35]
                    url_out = url_out.replace(old_chkin, str(date_chkin))
                    url_out = url_out.replace(old_chout, str(date_chout))
                    print(url_out)
            posicion += 1
        elif i == "?" and cycle == 2:
            date_chkin = date.today() + timedelta(days=30)
            date_chout = date.today() + timedelta(days=31)
            old_chkin = ""
            old_chout = ""

            for ch in url_out:
                #print(ch, url_out[posicion], posicion)
                #print(url_out[posicion+1:posicion+6])
                if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
                    old_chkin = url_out[posicion+7:posicion+17]
                    old_chout = url_out[posicion+25:posicion+35]
                    url_out = url_out.replace(old_chkin, str(date_chkin))
                    url_out = url_out.replace(old_chout, str(date_chout))
                    print(url_out)
            posicion += 1
        elif i == "?" and cycle == 3:
            date_chkin = date.today() + timedelta(days=90)
            date_chout = date.today() + timedelta(days=91)
            old_chkin = ""
            old_chout = ""

            for ch in url_out:
                #print(ch, url_out[posicion], posicion)
                #print(url_out[posicion+1:posicion+6])
                if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
                    old_chkin = url_out[posicion+7:posicion+17]
                    old_chout = url_out[posicion+25:posicion+35]
                    url_out = url_out.replace(old_chkin, str(date_chkin))
                    url_out = url_out.replace(old_chout, str(date_chout))
                    print(url_out)
            posicion += 1
    return url

url_out = "https://www.expedia.mx/Playa-Del-Carmen-Hoteles-Grand-Velas-Riviera-Maya-All-Inclusive.h2406344.Informacion-Hotel?chkin=2023-07-05&chkout=2023-07-06&x_pwa=1&rfrr=HSR&pwa_ts=1687358143606&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5teC9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=601751&destination=Playa+del+Carmen%2C+Quintana+Roo%2C+México&destType=MARKET&latLong=20.629571%2C-87.073173&trackingData=AAAAAQAAAAEAAAAQ4qf01Y8r0o2gOQgXXj0KEzRUHzRddpOI5GcD1i7H3XXfCpUzmz0ZO3q4myp4hx2mrz_38jYZWTSvps0_N2rQWJf3y1csihBYIue3x_Tv2r1eh6apcjzZr8M6CWZ8elmogXNaAyZmiIlsCqsA1KyhbZvuWDA1FWyP0bvhCXXlwhk1VuuiNA4pZQuyknHG4FbzKmVy0LSO3iQ3oyqL0y9ufeCC0bpK8YhDBiu7xrY9K3h2UwrskW2Fp7u92KWnXQnUhUa4p1bHzgumXsBXp_EKbeu6UtmTBSOVU47R23u13Yul0huDoa-KzjfEKoBkoDt9Q4CfLiqot3hd3TZkljrx6CTNJhsv6MB_-Xr8pXA0LRKR8CG_YZQzlxxlPv0uOpB-1NFqGdgBqauo1rnQelkBHS-yGIrZrcI_eeGI4UJek7yV3tVZrPyPU6HpqwmXBuD2LMlNHpRw98amQC_-5O454EDZ6l7KOX-YlRYiJeKm4EgK46_kpa38BiAR_Xfv-q2784P2ARbsVrRTyKV4vBWWyZIaiM1DmajwneYsr_bg-uvEPKi09w0qg8RNLbC3y059sdv5850_4wgQO7b7Gypbs2krpSThc8vXuhL1QcTIx_O1xy9D34AlVrImZyj2MSSiHWYRr5iYjx6gjo4cm8jzkxGgFdoRoVz0Oc4zwWIKuEBrzW3yGBscifToGvQeb3LFA_XJUAc9MA7QP8zl9Ji6lLvb73hWzPVByoCG-kg-H1E-WAR7xonqeomsTdsXiIqS_-TpY9nJuQPRS5QTJRkXNKdwZZTh0HZ4iLOHk0RvGkJgWYaPysM_SFomiMTzD3OJgtMzARL7GcSqPyA_QCL4ivcwStQ3Yw4DHumdzLdbXZ4k5GUWyHULH5yC29WGuEP98sq5Ov8KWBDC56yVuzyoMc_-OETBMM6_XV7EVPPS4F6p2V2wfcrjmr8W-hsh9to2Gh41RQLt8UDnlZQhVx8JAlT9950PHiRVZGu6vEPeR-F-CJwqEkiXFIY08B8b98fmr4ynpHEQU7w5LuJLK_ja5ic8NJq4qhw2K0baDZX6T8njFfYz6ZUR3vIwAAsBNgYaVXTEcaVgmwnpoXLJZaCcOObF7rNKtuRXJZDMXt1mQ7DVcjtUe88wM4A9V48I32Kq_HcrP9LIBUbSCNVP59D2ie5hHLx-J8T_8Q50vlHBuCIx1J6e-qxqMOa505WMXejPEzDFG8Sn4Z_rVSArDXk_4B3CkuXRRlNe3uhFxkA5KFRlwO93FQZT_0lKZ1rxGXpc7kzm7zIS9HE8cy5g-BDJm6DvxQAi2sAwGDZttGaO_b6ZMmsZAuxZNg8lAhW4wU_DEzDe62v69jixcTZIDFoMH8P0AUcH2oRvLEkRJ3Kh0HU1NiO2ugDZ4kQ2ZBOkBcOexCJJ1dhEF-k7zb7aOGvEI4SOlOu0YX_OqJri_8tbGa90rhR8QtCg-P4RA0GRQ3MXVAoeOw2PrDajjkR_IF5-kWF9WTKvHevhLhlqxZHa1dgWc0TEoU2n_4HiOY6DceSzoU6fEUMF8A9l78O8wFAnshWMLBhbMlKj_ddAPMv6a2IMfZkKN0zvD4TDOBRzkSplAqO9T9c8tMFTbi8PzG10QO32m1xcxrtMVq5cZS4wf9cwFMZfKwIC1za1VQ_Rbko6mLlrl4EhLbJ9MzTbYx-C6nPlZNPeFgYPJTLDAqe1PpsajLyLkbEu5toGjrOmaIqOivEME06pVwUJHV2H5HM3pvo-1gZrYaXw0reY7oGTGPgXeInIIkn9Bsm8tXx4jRRDSAaqQAQDX5TrwGhERdXU7-bz_Jwwulqy2RI7faFr27L2jVNCB0L2gX6tkI9LhHiSwy74MnViq6cbTniWuJbL92FbOikRH-XRz41Im3kN0cPaig3XCtvOJE3jn1SfuNIXzRXs8-mUv6nC22LgsguSwxDLGuqRWgqBY7TJ5TIqyEVcwQ2rEQuEixcfp6WfaomZyfTYfbzXevlFtO352tTfL7DiJFVfQgvwx8oicXzq8GsG0_uZNU3cI8n61gHbad9uIsfcMuaifURLF2dND2BXclKYw9d8xYA2gewnXp8U_juR6ZxELmjmblUXg8A7tduamKb-J5DBcjNdT6E-2fkef5fMNyM9SKvSYztITZsKtMjCbUvqCfTcjpvAsaMPPyLRvGPDMlJP8SS16qqR0qlTtKbggnXHZckEaT0K6v6w4Deb4vaacuVoRJz9ICIAm6yoy1xU52_lwZMTBljdoHtTmPIBJ9ENiFK49npkNqcSOMK_baOcBkVBtnNv_ucdfPQ71wW3RiNaDx6WuKg5FRJD5RiaJ5eDXcDCn-DmE1ywZLes0FFkXON1PrFNvmyhhTNYVg1kP_4udvMBYJD-0xmkeDCmHakEi_kdvw9lk29QUn1ZiXTdmGsoMSm08C1Qp06b14iZVIMB-lEDla-nXaXkeA%3D%3D&rank=1&testVersionOverride=Buttercup%2C45803.145008.1%2C44204.0.0%2C44203.0.0%2C43549.0.0%2C43550.0.0%2C31936.102311.0%2C33775.98848.1%2C38414.114301.0%2C39483.0.0%2C38427.115718.1%2C42444.0.0%2C42589.0.0%2C42876.124673.0%2C42973.0.0%2C42974.0.0%2C42975.0.0%2C42976.0.0%2C42802.125960.1%2C33739.99567.0%2C37898.109354.0%2C37930.0.0%2C37949.0.0%2C37354.0.0%2C43435.128144.0%2C43153.133019.3&slots=&position=1&beaconIssued=&sort=RECOMMENDED&top_dp=16727&top_cur=MXN&userIntent=&selectedRoomType=210311669&selectedRatePlan=222288917&searchId=8aa188bd-a172-46e6-a1fa-fa41b3c1aab7"

date_chkin = date.today() + timedelta(days=1)
date_chout = date.today() + timedelta(days=2)
old_chkin = ""
old_chout = ""

for ch in url_out:
    #print(ch, url_out[posicion], posicion)
    #print(url_out[posicion+1:posicion+6])
    if ch == "?" and url_out[posicion+1:posicion+6] == "chkin":
        old_chkin = url_out[posicion+7:posicion+17]
        old_chout = url_out[posicion+25:posicion+35]
        url_out = url_out.replace(old_chkin, str(date_chkin))
        url_out = url_out.replace(old_chout, str(date_chout))
        print(url_out)
    posicion += 1


#new_url = url_out[posicion+6:posicion+16] = date_chkin
#print(new_url)
    
# url_convert(url_out, cycle_out)


# Create your tests here.