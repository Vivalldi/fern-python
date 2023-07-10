# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CurrencyCode(str, enum.Enum):
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYN = "BYN"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRU = "MRU"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    CNY = "CNY"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLE = "SLE"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STN = "STN"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    USN = "USN"
    UYI = "UYI"
    UYU = "UYU"
    UYW = "UYW"
    UZS = "UZS"
    VED = "VED"
    VES = "VES"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XBA = "XBA"
    XBB = "XBB"
    XBC = "XBC"
    XBD = "XBD"
    XCD = "XCD"
    XDR = "XDR"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    XPT = "XPT"
    XSU = "XSU"
    XTS = "XTS"
    XUA = "XUA"
    XXX = "XXX"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"
    ZWL = "ZWL"

    def visit(
        self,
        aed: typing.Callable[[], T_Result],
        afn: typing.Callable[[], T_Result],
        all: typing.Callable[[], T_Result],
        amd: typing.Callable[[], T_Result],
        ang: typing.Callable[[], T_Result],
        aoa: typing.Callable[[], T_Result],
        ars: typing.Callable[[], T_Result],
        aud: typing.Callable[[], T_Result],
        awg: typing.Callable[[], T_Result],
        azn: typing.Callable[[], T_Result],
        bam: typing.Callable[[], T_Result],
        bbd: typing.Callable[[], T_Result],
        bdt: typing.Callable[[], T_Result],
        bgn: typing.Callable[[], T_Result],
        bhd: typing.Callable[[], T_Result],
        bif: typing.Callable[[], T_Result],
        bmd: typing.Callable[[], T_Result],
        bnd: typing.Callable[[], T_Result],
        bob: typing.Callable[[], T_Result],
        bov: typing.Callable[[], T_Result],
        brl: typing.Callable[[], T_Result],
        bsd: typing.Callable[[], T_Result],
        btn: typing.Callable[[], T_Result],
        bwp: typing.Callable[[], T_Result],
        byn: typing.Callable[[], T_Result],
        bzd: typing.Callable[[], T_Result],
        cad: typing.Callable[[], T_Result],
        cdf: typing.Callable[[], T_Result],
        che: typing.Callable[[], T_Result],
        chf: typing.Callable[[], T_Result],
        chw: typing.Callable[[], T_Result],
        clf: typing.Callable[[], T_Result],
        clp: typing.Callable[[], T_Result],
        cop: typing.Callable[[], T_Result],
        cou: typing.Callable[[], T_Result],
        crc: typing.Callable[[], T_Result],
        cuc: typing.Callable[[], T_Result],
        cup: typing.Callable[[], T_Result],
        cve: typing.Callable[[], T_Result],
        czk: typing.Callable[[], T_Result],
        djf: typing.Callable[[], T_Result],
        dkk: typing.Callable[[], T_Result],
        dop: typing.Callable[[], T_Result],
        dzd: typing.Callable[[], T_Result],
        egp: typing.Callable[[], T_Result],
        ern: typing.Callable[[], T_Result],
        etb: typing.Callable[[], T_Result],
        eur: typing.Callable[[], T_Result],
        fjd: typing.Callable[[], T_Result],
        fkp: typing.Callable[[], T_Result],
        gbp: typing.Callable[[], T_Result],
        gel: typing.Callable[[], T_Result],
        ghs: typing.Callable[[], T_Result],
        gip: typing.Callable[[], T_Result],
        gmd: typing.Callable[[], T_Result],
        gnf: typing.Callable[[], T_Result],
        gtq: typing.Callable[[], T_Result],
        gyd: typing.Callable[[], T_Result],
        hkd: typing.Callable[[], T_Result],
        hnl: typing.Callable[[], T_Result],
        htg: typing.Callable[[], T_Result],
        huf: typing.Callable[[], T_Result],
        idr: typing.Callable[[], T_Result],
        ils: typing.Callable[[], T_Result],
        inr: typing.Callable[[], T_Result],
        iqd: typing.Callable[[], T_Result],
        irr: typing.Callable[[], T_Result],
        isk: typing.Callable[[], T_Result],
        jmd: typing.Callable[[], T_Result],
        jod: typing.Callable[[], T_Result],
        jpy: typing.Callable[[], T_Result],
        kes: typing.Callable[[], T_Result],
        kgs: typing.Callable[[], T_Result],
        khr: typing.Callable[[], T_Result],
        kmf: typing.Callable[[], T_Result],
        kpw: typing.Callable[[], T_Result],
        krw: typing.Callable[[], T_Result],
        kwd: typing.Callable[[], T_Result],
        kyd: typing.Callable[[], T_Result],
        kzt: typing.Callable[[], T_Result],
        lak: typing.Callable[[], T_Result],
        lbp: typing.Callable[[], T_Result],
        lkr: typing.Callable[[], T_Result],
        lrd: typing.Callable[[], T_Result],
        lsl: typing.Callable[[], T_Result],
        lyd: typing.Callable[[], T_Result],
        mad: typing.Callable[[], T_Result],
        mdl: typing.Callable[[], T_Result],
        mga: typing.Callable[[], T_Result],
        mkd: typing.Callable[[], T_Result],
        mmk: typing.Callable[[], T_Result],
        mnt: typing.Callable[[], T_Result],
        mop: typing.Callable[[], T_Result],
        mru: typing.Callable[[], T_Result],
        mur: typing.Callable[[], T_Result],
        mvr: typing.Callable[[], T_Result],
        mwk: typing.Callable[[], T_Result],
        mxn: typing.Callable[[], T_Result],
        mxv: typing.Callable[[], T_Result],
        myr: typing.Callable[[], T_Result],
        mzn: typing.Callable[[], T_Result],
        nad: typing.Callable[[], T_Result],
        ngn: typing.Callable[[], T_Result],
        nio: typing.Callable[[], T_Result],
        nok: typing.Callable[[], T_Result],
        npr: typing.Callable[[], T_Result],
        nzd: typing.Callable[[], T_Result],
        omr: typing.Callable[[], T_Result],
        pab: typing.Callable[[], T_Result],
        pen: typing.Callable[[], T_Result],
        pgk: typing.Callable[[], T_Result],
        php: typing.Callable[[], T_Result],
        pkr: typing.Callable[[], T_Result],
        pln: typing.Callable[[], T_Result],
        pyg: typing.Callable[[], T_Result],
        qar: typing.Callable[[], T_Result],
        ron: typing.Callable[[], T_Result],
        rsd: typing.Callable[[], T_Result],
        cny: typing.Callable[[], T_Result],
        rub: typing.Callable[[], T_Result],
        rwf: typing.Callable[[], T_Result],
        sar: typing.Callable[[], T_Result],
        sbd: typing.Callable[[], T_Result],
        scr: typing.Callable[[], T_Result],
        sdg: typing.Callable[[], T_Result],
        sek: typing.Callable[[], T_Result],
        sgd: typing.Callable[[], T_Result],
        shp: typing.Callable[[], T_Result],
        sle: typing.Callable[[], T_Result],
        sll: typing.Callable[[], T_Result],
        sos: typing.Callable[[], T_Result],
        srd: typing.Callable[[], T_Result],
        ssp: typing.Callable[[], T_Result],
        stn: typing.Callable[[], T_Result],
        svc: typing.Callable[[], T_Result],
        syp: typing.Callable[[], T_Result],
        szl: typing.Callable[[], T_Result],
        thb: typing.Callable[[], T_Result],
        tjs: typing.Callable[[], T_Result],
        tmt: typing.Callable[[], T_Result],
        tnd: typing.Callable[[], T_Result],
        top: typing.Callable[[], T_Result],
        try_: typing.Callable[[], T_Result],
        ttd: typing.Callable[[], T_Result],
        twd: typing.Callable[[], T_Result],
        tzs: typing.Callable[[], T_Result],
        uah: typing.Callable[[], T_Result],
        ugx: typing.Callable[[], T_Result],
        usd: typing.Callable[[], T_Result],
        usn: typing.Callable[[], T_Result],
        uyi: typing.Callable[[], T_Result],
        uyu: typing.Callable[[], T_Result],
        uyw: typing.Callable[[], T_Result],
        uzs: typing.Callable[[], T_Result],
        ved: typing.Callable[[], T_Result],
        ves: typing.Callable[[], T_Result],
        vnd: typing.Callable[[], T_Result],
        vuv: typing.Callable[[], T_Result],
        wst: typing.Callable[[], T_Result],
        xaf: typing.Callable[[], T_Result],
        xag: typing.Callable[[], T_Result],
        xau: typing.Callable[[], T_Result],
        xba: typing.Callable[[], T_Result],
        xbb: typing.Callable[[], T_Result],
        xbc: typing.Callable[[], T_Result],
        xbd: typing.Callable[[], T_Result],
        xcd: typing.Callable[[], T_Result],
        xdr: typing.Callable[[], T_Result],
        xof: typing.Callable[[], T_Result],
        xpd: typing.Callable[[], T_Result],
        xpf: typing.Callable[[], T_Result],
        xpt: typing.Callable[[], T_Result],
        xsu: typing.Callable[[], T_Result],
        xts: typing.Callable[[], T_Result],
        xua: typing.Callable[[], T_Result],
        xxx: typing.Callable[[], T_Result],
        yer: typing.Callable[[], T_Result],
        zar: typing.Callable[[], T_Result],
        zmw: typing.Callable[[], T_Result],
        zwl: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CurrencyCode.AED:
            return aed()
        if self is CurrencyCode.AFN:
            return afn()
        if self is CurrencyCode.ALL:
            return all()
        if self is CurrencyCode.AMD:
            return amd()
        if self is CurrencyCode.ANG:
            return ang()
        if self is CurrencyCode.AOA:
            return aoa()
        if self is CurrencyCode.ARS:
            return ars()
        if self is CurrencyCode.AUD:
            return aud()
        if self is CurrencyCode.AWG:
            return awg()
        if self is CurrencyCode.AZN:
            return azn()
        if self is CurrencyCode.BAM:
            return bam()
        if self is CurrencyCode.BBD:
            return bbd()
        if self is CurrencyCode.BDT:
            return bdt()
        if self is CurrencyCode.BGN:
            return bgn()
        if self is CurrencyCode.BHD:
            return bhd()
        if self is CurrencyCode.BIF:
            return bif()
        if self is CurrencyCode.BMD:
            return bmd()
        if self is CurrencyCode.BND:
            return bnd()
        if self is CurrencyCode.BOB:
            return bob()
        if self is CurrencyCode.BOV:
            return bov()
        if self is CurrencyCode.BRL:
            return brl()
        if self is CurrencyCode.BSD:
            return bsd()
        if self is CurrencyCode.BTN:
            return btn()
        if self is CurrencyCode.BWP:
            return bwp()
        if self is CurrencyCode.BYN:
            return byn()
        if self is CurrencyCode.BZD:
            return bzd()
        if self is CurrencyCode.CAD:
            return cad()
        if self is CurrencyCode.CDF:
            return cdf()
        if self is CurrencyCode.CHE:
            return che()
        if self is CurrencyCode.CHF:
            return chf()
        if self is CurrencyCode.CHW:
            return chw()
        if self is CurrencyCode.CLF:
            return clf()
        if self is CurrencyCode.CLP:
            return clp()
        if self is CurrencyCode.COP:
            return cop()
        if self is CurrencyCode.COU:
            return cou()
        if self is CurrencyCode.CRC:
            return crc()
        if self is CurrencyCode.CUC:
            return cuc()
        if self is CurrencyCode.CUP:
            return cup()
        if self is CurrencyCode.CVE:
            return cve()
        if self is CurrencyCode.CZK:
            return czk()
        if self is CurrencyCode.DJF:
            return djf()
        if self is CurrencyCode.DKK:
            return dkk()
        if self is CurrencyCode.DOP:
            return dop()
        if self is CurrencyCode.DZD:
            return dzd()
        if self is CurrencyCode.EGP:
            return egp()
        if self is CurrencyCode.ERN:
            return ern()
        if self is CurrencyCode.ETB:
            return etb()
        if self is CurrencyCode.EUR:
            return eur()
        if self is CurrencyCode.FJD:
            return fjd()
        if self is CurrencyCode.FKP:
            return fkp()
        if self is CurrencyCode.GBP:
            return gbp()
        if self is CurrencyCode.GEL:
            return gel()
        if self is CurrencyCode.GHS:
            return ghs()
        if self is CurrencyCode.GIP:
            return gip()
        if self is CurrencyCode.GMD:
            return gmd()
        if self is CurrencyCode.GNF:
            return gnf()
        if self is CurrencyCode.GTQ:
            return gtq()
        if self is CurrencyCode.GYD:
            return gyd()
        if self is CurrencyCode.HKD:
            return hkd()
        if self is CurrencyCode.HNL:
            return hnl()
        if self is CurrencyCode.HTG:
            return htg()
        if self is CurrencyCode.HUF:
            return huf()
        if self is CurrencyCode.IDR:
            return idr()
        if self is CurrencyCode.ILS:
            return ils()
        if self is CurrencyCode.INR:
            return inr()
        if self is CurrencyCode.IQD:
            return iqd()
        if self is CurrencyCode.IRR:
            return irr()
        if self is CurrencyCode.ISK:
            return isk()
        if self is CurrencyCode.JMD:
            return jmd()
        if self is CurrencyCode.JOD:
            return jod()
        if self is CurrencyCode.JPY:
            return jpy()
        if self is CurrencyCode.KES:
            return kes()
        if self is CurrencyCode.KGS:
            return kgs()
        if self is CurrencyCode.KHR:
            return khr()
        if self is CurrencyCode.KMF:
            return kmf()
        if self is CurrencyCode.KPW:
            return kpw()
        if self is CurrencyCode.KRW:
            return krw()
        if self is CurrencyCode.KWD:
            return kwd()
        if self is CurrencyCode.KYD:
            return kyd()
        if self is CurrencyCode.KZT:
            return kzt()
        if self is CurrencyCode.LAK:
            return lak()
        if self is CurrencyCode.LBP:
            return lbp()
        if self is CurrencyCode.LKR:
            return lkr()
        if self is CurrencyCode.LRD:
            return lrd()
        if self is CurrencyCode.LSL:
            return lsl()
        if self is CurrencyCode.LYD:
            return lyd()
        if self is CurrencyCode.MAD:
            return mad()
        if self is CurrencyCode.MDL:
            return mdl()
        if self is CurrencyCode.MGA:
            return mga()
        if self is CurrencyCode.MKD:
            return mkd()
        if self is CurrencyCode.MMK:
            return mmk()
        if self is CurrencyCode.MNT:
            return mnt()
        if self is CurrencyCode.MOP:
            return mop()
        if self is CurrencyCode.MRU:
            return mru()
        if self is CurrencyCode.MUR:
            return mur()
        if self is CurrencyCode.MVR:
            return mvr()
        if self is CurrencyCode.MWK:
            return mwk()
        if self is CurrencyCode.MXN:
            return mxn()
        if self is CurrencyCode.MXV:
            return mxv()
        if self is CurrencyCode.MYR:
            return myr()
        if self is CurrencyCode.MZN:
            return mzn()
        if self is CurrencyCode.NAD:
            return nad()
        if self is CurrencyCode.NGN:
            return ngn()
        if self is CurrencyCode.NIO:
            return nio()
        if self is CurrencyCode.NOK:
            return nok()
        if self is CurrencyCode.NPR:
            return npr()
        if self is CurrencyCode.NZD:
            return nzd()
        if self is CurrencyCode.OMR:
            return omr()
        if self is CurrencyCode.PAB:
            return pab()
        if self is CurrencyCode.PEN:
            return pen()
        if self is CurrencyCode.PGK:
            return pgk()
        if self is CurrencyCode.PHP:
            return php()
        if self is CurrencyCode.PKR:
            return pkr()
        if self is CurrencyCode.PLN:
            return pln()
        if self is CurrencyCode.PYG:
            return pyg()
        if self is CurrencyCode.QAR:
            return qar()
        if self is CurrencyCode.RON:
            return ron()
        if self is CurrencyCode.RSD:
            return rsd()
        if self is CurrencyCode.CNY:
            return cny()
        if self is CurrencyCode.RUB:
            return rub()
        if self is CurrencyCode.RWF:
            return rwf()
        if self is CurrencyCode.SAR:
            return sar()
        if self is CurrencyCode.SBD:
            return sbd()
        if self is CurrencyCode.SCR:
            return scr()
        if self is CurrencyCode.SDG:
            return sdg()
        if self is CurrencyCode.SEK:
            return sek()
        if self is CurrencyCode.SGD:
            return sgd()
        if self is CurrencyCode.SHP:
            return shp()
        if self is CurrencyCode.SLE:
            return sle()
        if self is CurrencyCode.SLL:
            return sll()
        if self is CurrencyCode.SOS:
            return sos()
        if self is CurrencyCode.SRD:
            return srd()
        if self is CurrencyCode.SSP:
            return ssp()
        if self is CurrencyCode.STN:
            return stn()
        if self is CurrencyCode.SVC:
            return svc()
        if self is CurrencyCode.SYP:
            return syp()
        if self is CurrencyCode.SZL:
            return szl()
        if self is CurrencyCode.THB:
            return thb()
        if self is CurrencyCode.TJS:
            return tjs()
        if self is CurrencyCode.TMT:
            return tmt()
        if self is CurrencyCode.TND:
            return tnd()
        if self is CurrencyCode.TOP:
            return top()
        if self is CurrencyCode.TRY:
            return try_()
        if self is CurrencyCode.TTD:
            return ttd()
        if self is CurrencyCode.TWD:
            return twd()
        if self is CurrencyCode.TZS:
            return tzs()
        if self is CurrencyCode.UAH:
            return uah()
        if self is CurrencyCode.UGX:
            return ugx()
        if self is CurrencyCode.USD:
            return usd()
        if self is CurrencyCode.USN:
            return usn()
        if self is CurrencyCode.UYI:
            return uyi()
        if self is CurrencyCode.UYU:
            return uyu()
        if self is CurrencyCode.UYW:
            return uyw()
        if self is CurrencyCode.UZS:
            return uzs()
        if self is CurrencyCode.VED:
            return ved()
        if self is CurrencyCode.VES:
            return ves()
        if self is CurrencyCode.VND:
            return vnd()
        if self is CurrencyCode.VUV:
            return vuv()
        if self is CurrencyCode.WST:
            return wst()
        if self is CurrencyCode.XAF:
            return xaf()
        if self is CurrencyCode.XAG:
            return xag()
        if self is CurrencyCode.XAU:
            return xau()
        if self is CurrencyCode.XBA:
            return xba()
        if self is CurrencyCode.XBB:
            return xbb()
        if self is CurrencyCode.XBC:
            return xbc()
        if self is CurrencyCode.XBD:
            return xbd()
        if self is CurrencyCode.XCD:
            return xcd()
        if self is CurrencyCode.XDR:
            return xdr()
        if self is CurrencyCode.XOF:
            return xof()
        if self is CurrencyCode.XPD:
            return xpd()
        if self is CurrencyCode.XPF:
            return xpf()
        if self is CurrencyCode.XPT:
            return xpt()
        if self is CurrencyCode.XSU:
            return xsu()
        if self is CurrencyCode.XTS:
            return xts()
        if self is CurrencyCode.XUA:
            return xua()
        if self is CurrencyCode.XXX:
            return xxx()
        if self is CurrencyCode.YER:
            return yer()
        if self is CurrencyCode.ZAR:
            return zar()
        if self is CurrencyCode.ZMW:
            return zmw()
        if self is CurrencyCode.ZWL:
            return zwl()
