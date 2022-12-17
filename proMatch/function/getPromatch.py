import requests
from pprint import pprint
import json

KEY = "RGAPI-88ac3bfa-6138-474a-9fe0-83d835caaa57"
baseUrl = "https://asia.api.riotgames.com"

proPUUID = ['aYZCUruerjylcvYZlQDEr6d5r-MxjuKUG-breok6JQbWl3csfiwkpr46fjJfV8iulB-8EVs8liBZRA',
            'uiQdP9LWly-2ZAQjoSGqvUlMLiUkaZPwdd3dis0QZkmgTf9UsYsl3OJkt0zczJe-z_f70AhMmm5fUQ',
            '7Jee8T-FWQD7HZR6DZugWYYLkiVy1VeQ55vFzMp0n9WJ9wUWmJrcPWQn9oV-8bo34kkN5f2fnkZSHw',
            '5TM5YhnUWMCtDpc-HCF6t1cTyESOA9dZbvDJuQdS6C6km9oUR24_5LDNu1NSAhV4gHHa_UHdqzevkQ',
            'ew6BBeL2-R3NJH5V0MzzRnaYavA3VqXbKmxsxG_V6dBlzOSBWJT4jbhdw3Pcj09bxA9BA57SqjFdvA',
            'd_F8dl7iqixgAPfeFvf2dNeVOvsH2Xqs6Mn8fq2-0rYPFBBw9-t9_y0igFzxl8LpAj6L_6qLXMD5-A',
            'eJkJMaE7sf7mCRasR94ly579qU0D_5fCvkLnCOiPHOJVpLLXM3mfCmbHAgR3bfPpoFKFZMHcdXx0kA',
            'ExDKfpIhvpNOWow3D1OYXQ-KFdK81HVFwaLrjWOVPxTdWEP_3mEuxOEw1bznegWMB5hl2lZ_nn1zDA',
            'bgc7zhpQYSAmdGEhFirMBVj_MQ1j2I6tL95oR_islXzLNpZJugxat98RM4hxdw6KsfnI79MkPQ8oFQ',
            'eu4zIDsIMs5wmQAjL1zKv5SxDVSZ32zolnMfZuMMdRw5vix1qa617bp8G_H8-T4me3GhcLhEZQcejw',
            'rfXqBXzVf_BTYY3VUTGA3v-vkAOYUwT9KtMpVewPPcq2JD0bAth5_8zcadUE30IHdcq6xRe8-7ET9Q',
            '2J7lMvlfczhPlt8SMl4khh2YbdhdBG0pjfMGBy_ePYBgWtF6HdM1CXkMgPHNm7idsswcSsN2wrh9CQ',
            '1JP6GeMYXBesfYX005jD0eSbzZR2NGBBx2t43xGOR2RNi2GmTfGLmDXNQYPlkTueLa5fsgha1ZixPA',
            'xUQ5BCpkjDHYPQcQOcCrlB1fBV_rA-xARs6zzL50LUO8Yiyy_i3V_pu_Jxy1wrH7Cv_ekRNWnMuRbw',
            'DvVEIHxlSRJdwMS_W2Iofo1lwNVS8jb7SuuZww_kE-QLKXEbzBX1VIrUkFoH5qiPP_H10KbfvyxMww',
            'U2txH32ejt9_7O1uA4jrGGTfDF-RqrDOCIRsJKX2crjo7COwFFCKdJ7LvL02Y2O50H8aUmvcMoQr9Q',
            'ReX22smR5FpPaHCx-jmyv_PdFBxlwyzi4N6i_bDuZKIdWN0SbpEAO3bZxXOjHZXpwFIV6gbKhXvOLw',
            '0r9oaB6WdbhzNQhuOexc-Q1kGEhQL23RP4bFfaPJX1dvG9icvXg73t_0STR4SIFc90O27_Hisot9MA',
            'CbJDYuakh2qb9rElD4mZfrQvbY10pomPVdCdw-0HQfQS1kRV7ggjj7pWeJ0R0cL0fyVYD3uQfVvjpw',
            'U7v2Yz8XR1_CIZYJGsY6dv9LbKKNmgACnuFh0qV0PSuCUIgxATwinTNiUrtnYDvAROqrHXqPIkvUCg',
            'J1z-_6lyrX-WzUrdnK0_ICkmjo-lzY4Eo_4NqiuVFUQDVcDR-C1sma_d4KGzUD6v2s7d9-iCO9bVzw',
            '1DLrEFUVVS41SVxqZStf6v8rfB1Fi0Bwqzpm4-a0hjv0fgFG3jHwJaYcJZ_wH84xYK22ItdbTALSgQ',
            'B1vTsT74jbgwimWJSjMkOq1TierFg-62j_aG6wry_60EcTPKoZBfDgOSLBq3g7Tqlu5Ps8ogRJsvCg',
            'JzpgvJdJ-URs8QSHO0Fl3OS7zaHFcZT14_X7dsNsMGuONSARyw2Ukprpx2SGS60yLfm7xCkB1AJEmg',
            'hZkVmp4JwsZVWq9zjFGEMxFVdluWxcDuQjLPWEMQmgKDZlBJKn4-6Tc-wMwbVWBx3GEjbteh2xpUnQ',
            '15chkNoiYKVNquTzcclkifaFFQzkWPdlgv34W4O2O1K2Xj9wtt9TRuGLPZ1UCDzkWIXfLTiY5EcC5w',
            'EO3UNnJT5quDvp-jhxehsfkD0BRabqLKnkGbVcRGsog7VkAmlulFDS3cs9M2tIp3sLTWaCbIM9jU6A',
            'IwknD0bCjclnHiYsrqDy8GGRTs4WFuTvZOgKU2P86BKPXHhgCaW-6yZ8p8Omo20H0ZvWceYQm0hJCw',
            'xtthqgcxBPZaoWMlNup0Bc_cXH_LYQ5y_bFpu_CnaU_F0__H6z20uPpoje4-sv2APnd1I6wiZl-JnA',
            'BdQT-SzrtpNAww1zIBtNyIlQvQtbpIF-g57ehkk_cn7_QXSfOD2Jm4VhERmmRxx12kBMKp4SLRY6rw',
            'uN5Zk1vXtwp3EfQJpvYX3fiuZ3Jt-u-f0qO4qA-YqtDTGafvbJ6nRxYJoFHbGs-pIoCZV81ToJLY0Q',
            'wllCGkMMsQrGatJ6_p7squCkW-QP1MtIoNeLQlbOy89XkeoJg1jbcKPJxLQv7WKmdw0I8q7kQ5T6jg',
            '2c6tGu1o464AMGZ4yYkwpfhDPQTl07E6PBAu8em5u-5OwUeSbn81qIzGctOFhI7mY_wYYo38G20xnQ',
            'ZDTjKGT4SfSatfKQ84MTiwr5kGTKh6cMc5lJGFcWqSbD7bMa9DQ5T00lX_j0v4DHsmN1cLP5sCN22g',
            'ERyhI7S4Xu0Kv8yziY-MVA7TnWI1mC-KyZJidcnMg9cxyvdvVpHJuqEnHlaor6RFFV8yRIc_RSao0A',
            'Z3qf5d3-eWgqEUojqCxTkzbL3Kom6EOYRJ3oHyMPk4j8wUnbt5UKWDAWvCWyY2_86-lr3vO8t6qk2w',
            'XEdN61ldGo-GxoeQCTzvvW5CYjQEHRgd6m48KE7LHUyDY58WGiBZ7PQ0IrH4OZhAGjYbTeXmUhm6rw',
            '0srfbgC880DAn61O4kEO69l1IFFZYgTIKqlC1Vx_fjkLL2xuWXOc_rRT8M7_eBQDeKFj4BIV_cvTSQ',
            'VMrBxE-zwVYab44rep565d372zhRIKCL5RUQleLqHsmU6m6Z4mivZWHcx9fQ6lwuTVmVRyBJYHVuPw',
            'Na6ESfAGicPdcCqUwU2Klc7tfTlRB_owz7Qtts95AwqavQNgZSDDbal9J1KKv4dsb8bJEttrFOhAFA',
            'hl0DtrJ6bxk8ukyMJDOP0Ogo-4xEqQLC6GuLgXFAJGVJHmp3_5BrJqezKnRX9gRAuh9dnkt3KNnMqA',
            '3yUF8DmmZjkeWMsaoMcW98hgVDzlIYiWb0GUCDDZyiVB2ScrWNLG8-_HfleLq6cnpIusyyD1tAiM2A',
            '18uO7zkQAxCpWVRUmzeW_myNxaYgLZ-Osc-hOgnBec5iINE4BkSXbQr5p99pQKW5PgldIiL-On66lQ',
            'v-F49A7muY_0k3nFCMLL8jDnZ_Q9GQUe1CmkgSzL5x_QxdWPriPu2Y6OACPBpuhsMdb4AogmMcstww',
            'Aar5z9befAyhtGJ7BlSwgwrUvzLcO8ETKy0pzOhw8MrVFzChscvQ8VGs9yO7JNmrKx6nsvK-9crD6Q',
            'vctv349OxJgsTvx_drE3OijRqKiBvvy73KbnqYqXBH8bE-H91xeHCwhJDOxnlIGJFqoIqoNTLHOgIQ',
            'DVKKKY3Z8anWGjJ73CaYaTemrQrEsn17weS244OJqfITZ0p0raz3HdErIO17Gv2fUBHI21Aps-u-qQ',
            'ZR0vFE6WOE5JZB7fNm7hnaF2tE1EsqP6EgGHyYyso2c0vsIDWENsS1XqM6eiEO2ap9VsUac4GVal8g',
            'ja0eQvC6zWOABhnf2ypkQ00o2uikmtda-DMv9dOKTPPshsJaZLboGTfnioMdEgs9qodzIdnMEMczYw',
            'a3AFcyRzcahYaC5QqXQeFiEnXdJkgH_UAvM1ib4L0fDtzKsHWig0kUTUX4ZaN2vQl9PwqEoZarJBCQ',
            'Lw4f8-B4zn-kghLTuPg40vF1SUhyXENndHqwHjiHLm1aEBgjYaY9DVRiuYYbdvBkdvPPOAW2okjjNw',
            '_Q_O2_1pKQgKsioSa_CI6hdGqdEXYn-C8WmpeiLVzhrJ2JHUBn5c3LXK3BVRFEKShr375VeHfULmAQ',
            '9C26C0XXzWxlC7FZRbargJfrpUQaoKSohLW8B7OSbdfs2e0BrneEZ1gxuiC8vZOtODBEQKcIlwx-Yw',
            'yBD_li4vJt-GG6PCSF81pjeEDBESBfbrLaVd8EGDatUw97NwSWsSehBLT1VScFSxBCkEDDgslnU0uQ',
            'h3zZM1hMI8T3znDs7Gp3WtYBiMMG26Oa7xUKqtyOwhFFKZlMXarWCHJncYY1XwpdDh2jJD7fRwPXpg',
            'DpGk7hP80s9sc96NBI_U5wWl1XAvHaZQWe6-ZLeCYplro_XEvGrgUtrRF0-VCUBxuzVJvr3dsHBF8w',
            'lttfN_oGABzY280G2sLs9VhT9EPZbjQqNcIGMe-wCnPmmv-d9l0rmP_L-AACG_AoAtIOPUlo00RVuw',
            'NbbE_KPvCGqJ0fOYwm_Cxt1edMVI3Is5_S31aW06gM0M6HmA7pCCJTlum6TwZuzWOKmVjWWWkL_C7Q',
            'KFivp_DATE7dXZA8V-0IUlK47cC2T6h8X1_j2S52_r3x061mfwi60a5GG8fz1NF23jW-p5MhMBHv7g',
            'PljrW7vZZ63zTuexw4EhjRwyF0Kl7uQY9RY0XRu9vC8f91fHJAjEiLqVDLepkC2565tYCTq2DQdy1g',
            'e7bnhI4F1ydgSIvGZb_IFyGdEOqIqWKY7LZPLpYgRqHsv8J2-TkUSXMose5-MZUIbe6Ov4191gmBqg',
            'dO4GfFvL7WlvMV2jzf_Dec2KnHJBSIwm9IIDQo3vzp7qNJGOpRRtcdR4sGM87aii5mHFVrrWjx0Qvw',
            'FWD3aK-z1ze0KzbaOh1Higc0VENk-uvJkHmVUSoErp0Ooml1m1yv2RTUXa6BKD2KZhRdgHEwQd-OmQ',
            'Bp516thwtkFzJt1wuOUWpbn2_lmle5CGzO0rzDOVBDIck2bug0wzgEHr3xLikCpaqQ1gJfwGZsmRyA',
            'fUvXV34DdXjHk9gBWMInMXGwO7gq6oOsdRHkLAqvAO6TQuaDrqh_oqC9ktg1gq5xF7sFmt-XklJdmA',
            'YRZa2huUTivA32_DaHoyEdSL4pULVg7x0RuliSSu4Jn52_6pe-VDmoKDJMkJfvQmKPE53m7N7DcIag',
            'tyzZEp2vn1CSx-G-6nOzY5y5Na9r_mGrES51RlE2udzxPuyHXEoru_Z63FCio9GOQNurYsVGUcSLrQ',
            'TjJmLu0U9-flWo2p7_dD1P-VA1tcsCjqhqlmfibM1lApEBDD4SFgEax9szsGtuAQ7oIlOfS-qNoHjQ',
            'a8oO0TjjrTazdyPVeGcsI1AZuFVJvuAc3ZEBJ9ELi2viM2H011Hkqlez41uBbNzU19fMAVNA5mecLg',
            'HjdDq1UMb7EZQzOcLFYDOcMYnQt8DbA8zLpnbfzZ2vT81rG3TYV4d6u6-7hVzc9dvPQK0Wp3uu6Eng',
            'QURNaQl6x2P9pZ6lIieRtARhNR1u-6Nls0BAN4nmkjfPx_znnq8zA2iY3MFa0wN_2a3LrQZVZAI4uQ',
            'uMcwft3F5kVda1m9LF03973hBoGIhzqycFz7gutG7DLweeYJqzmn650UVdHxRFSOCQDVRT4o5s1nog',
            'udMXMarxh4MjbNEg0O1GlIxgn9IqCy0R4YsUDfq1so_FKsD2lWEm7V0SyXkyu9ovMZn56lpX5QDMYQ',
            'kPLzT_Dk2FFk5IybliLn3-f7a2CpZKNumVra0xRO5uez8qo5LZp9wYBnDxCF6lQcUYvooGoktLbgDg',
            'aI8UTKJrAmSoahb7QaNH8-su_4uG8DzfPdsoEw-NPcLjkKOGZiGo9uixFD2Wj2ciJL5bb5Ge_6RMzw',
            'XbGxW1pXKSD9k_EnySz8Es8Ufs6gKF_2w-7r6wpjVMQtWQgNeu7Ims1659MXkmEIE5_GqVMkNBZD0A',
            'iRj8BwwNHP_BMLdB2jMCycxv9XrDTLe05G4KHEeJKqNSqmD6Bji0gaOqBKp-20CAxbj54VKjPWeZsw',
            'L6Ru3TiopZ2NhIQx_9sMUCkpTSWDnnMS3lRW9r84ZSr84k1XHQg0yfRJnFDI8hUqBvXitsoZkg_6eQ',
            'hWUSY25u3xIuEDrXKWMgV6cTpNMbSftSkFfIY9ClkxxaVtxVq-5E0J9Y1Yuv4jmILs4GvDLTzcEY_A',
            'HfvtfmMYAvp9M4k0k8akxBU-CdT7eh5h58IMIvRzkXFA71d45cDtPM-84RyWGFuBoqdHU668Z3RmMg',
            'FuhgQTdy5zl1YKaV5pFZI7VaQ7qj47gteha-HQWTl6HOaLUoj-wT71aAvfdwUewRBwl-RY7IXlLApg',
            'rlr6fYG1jNS2UL9TcFKXcdepD_-9Ehei145g7-9tOFp8MFi3QZ3NVNXi1Ql50Y-HbJYZEuwlwvpxPw',
            '9Ewem6UxxtHIpqXtz0Avnmgivtqy9SCAWW-SlkGTL9hrrk0AdY7L2wepeCuU_5hl7YP2i88TMogBog',
            'd9Ne0swR7y2q3Lkn-uqmYu7Y3-cVW6UR2bnTsIF-IMR5bMwVNhc4-MFy50hpAj62mcXln1NNK0h-iQ',
            'Y9YMFclvIHuJO0zqbljEMTWjpd9LSotyJKpSMdpPg24VNj0eKyU0mfDjap7YYvnz1V00ls2TFOVcUw',
            'EfRu2x4pex94bmK4Kokcs23CZCGnSAtieD9h-6Dx5tQY91bbwjD4sGbfdIDsHVoB7OerAzyY6s5K3w',
            'O0zy3YfLZ2nxIpQTjAwEg3ex7vK9Sd1NisrmclucuKAQIRnWlVxL9oTVkhR4R8dP4lNBhqhjgTiQ8A',
            'cUrhujyU6NF2dM_UzO4OKUJl9V9i0-cT0TStkEGB42LrKGXSUfhWl3ASJZpKdGqhWjlFkpohFtdyNg',
            'lgvqylJ7FiNSjwYFkQceQsVAcJhet26T8uvf3ESFCVs116N5rQxvxGJfhWl5h_deeQedf9eL1KiTdw',
            'jCo37iBcRKvj10DdF4F9AwzTC7x0jw_Y44YI_mCsJmuvoqYIg7v3ZWPV1Tn2QbdnoW38rkDnAR65pg',
            'GtsMN3t9pLrrrE8OKPbhr1x5tintw0oQ5ARbLQroD8dY01TxOHi5TR2_7UKqNYcFM1bv8avPRQcnwg',
            ]

f = open('proMatch.txt', 'r')

for pid in proPUUID:
    getMatchUrl = f'{baseUrl}/lol/match/v5/matches/by-puuid/{pid}/ids?start=0&count=20&api_key={KEY}'
    r = (requests.get(getMatchUrl).json())
    print(r)
    f.write(json.dumps(r), ", \n")

f.close()
