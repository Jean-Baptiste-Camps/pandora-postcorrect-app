from app.models import Corpus, WordToken, AllowedLemma, AllowedPOS, AllowedMorph

Floovant = Corpus(name="Floovant", id=2)
FloovantTokens = [
    WordToken(corpus=Floovant.id, form="SOIGNORS", lemma="seignor", context="SOIGNORS or escoutez que", label_uniform="seignor", morph="NOMB.=p|GENRE=m|CAS=n"),
    WordToken(corpus=Floovant.id, form="or", lemma="or4", context="SOIGNORS or escoutez que Dés", label_uniform="or4", morph="DEGRE=-"),
    WordToken(corpus=Floovant.id, form="escoutez", lemma="escouter", context="SOIGNORS or escoutez que Dés vos", label_uniform="escouter", morph="MODE=imp|PERS.=2|NOMB.=p"),
    WordToken(corpus=Floovant.id, form="que", lemma="que4", context="SOIGNORS or escoutez que Dés vos soit", label_uniform="que4", morph="_"),
    WordToken(corpus=Floovant.id, form="Dés", lemma="dieu", context="or escoutez que Dés vos soit amis", label_uniform="dieu", morph="NOMB.=s|GENRE=m|CAS=n"),
    WordToken(corpus=Floovant.id, form="vos", lemma="vos1", context="escoutez que Dés vos soit amis III", label_uniform="vos1", morph="PERS.=2|NOMB.=p|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="soit", lemma="estre1", context="que Dés vos soit amis III vers", label_uniform="estre1", morph="MODE=sub|TEMPS=pst|PERS.=3|NOMB.=s"),
    WordToken(corpus=Floovant.id, form="amis", lemma="ami", context="Dés vos soit amis III vers de", label_uniform="ami", morph="NOMB.=s|GENRE=m|CAS=n"),
    WordToken(corpus=Floovant.id, form="III", lemma="trois1", context="vos soit amis III vers de bone", label_uniform="trois1", morph="NOMB.=p|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="vers", lemma="vers1", context="soit amis III vers de bone estoire", label_uniform="vers1", morph="NOMB.=p|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="de", lemma="de", context="amis III vers de bone estoire se", label_uniform="de", morph="_"),
    WordToken(corpus=Floovant.id, form="bone", lemma="bon", context="III vers de bone estoire se je", label_uniform="bon", morph="NOMB.=s|GENRE=f|CAS=r|DEGRE=p"),
    WordToken(corpus=Floovant.id, form="estoire", lemma="estoire1", context="vers de bone estoire se je les", label_uniform="estoire1", morph="NOMB.=s|GENRE=f|CAS=r"),
    WordToken(corpus=Floovant.id, form="se", lemma="si", context="de bone estoire se je les vos", label_uniform="si", morph="DEGRE=-"),
    WordToken(corpus=Floovant.id, form="je", lemma="je", context="bone estoire se je les vos devis", label_uniform="je", morph="PERS.=1|NOMB.=s|GENRE=m|CAS=n"),
    WordToken(corpus=Floovant.id, form="les", lemma="il", context="estoire se je les vos devis Dou", label_uniform="il", morph="PERS.=3|NOMB.=p|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="vos", lemma="vos1", context="se je les vos devis Dou premier", label_uniform="vos1", morph="PERS.=2|NOMB.=p|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="devis", lemma="deviser", context="je les vos devis Dou premier roi", label_uniform="deviser", morph="MODE=ind|TEMPS=pst|PERS.=1|NOMB.=s"),
    WordToken(corpus=Floovant.id, form="Dou", lemma="de+le", context="les vos devis Dou premier roi de", label_uniform="de+le", morph="NOMB.=s|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="premier", lemma="premier", context="vos devis Dou premier roi de France", label_uniform="premier", morph="NOMB.=s|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="roi", lemma="roi2", context="devis Dou premier roi de France qui", label_uniform="roi2", morph="NOMB.=s|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="de", lemma="de", context="Dou premier roi de France qui crestïens", label_uniform="de", morph="_"),
    WordToken(corpus=Floovant.id, form="France", lemma="france", context="premier roi de France qui crestïens devint", label_uniform="france", morph="NOMB.=s|GENRE=f|CAS=r"),
    WordToken(corpus=Floovant.id, form="qui", lemma="qui", context="roi de France qui crestïens devint Cil", label_uniform="qui", morph="NOMB.=s|GENRE=m|CAS=n"),
    WordToken(corpus=Floovant.id, form="crestïens", lemma="crestiien", context="de France qui crestïens devint Cil ot", label_uniform="crestiien", morph="NOMB.=s|GENRE=m|CAS=n"),
    WordToken(corpus=Floovant.id, form="devint", lemma="devenir", context="France qui crestïens devint Cil ot non", label_uniform="devenir", morph="MODE=ind|TEMPS=psp|PERS.=3|NOMB.=s"),
    WordToken(corpus=Floovant.id, form="Cil", lemma="cel", context="qui crestïens devint Cil ot non Cloovis", label_uniform="cel", morph="NOMB.=s|GENRE=m|CAS=n"),
    WordToken(corpus=Floovant.id, form="ot", lemma="avoir", context="crestïens devint Cil ot non Cloovis si", label_uniform="avoir", morph="MODE=ind|TEMPS=psp|PERS.=3|NOMB.=s"),
    WordToken(corpus=Floovant.id, form="non", lemma="nom", context="devint Cil ot non Cloovis si com", label_uniform="nom", morph="NOMB.=s|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="Cloovis", lemma="clovis", context="Cil ot non Cloovis si com truis", label_uniform="clovis", morph="NOMB.=s|GENRE=m|CAS=r"),
    WordToken(corpus=Floovant.id, form="si", lemma="si", context="ot non Cloovis si com truis en", label_uniform="si", morph="DEGRE=-"),
    WordToken(corpus=Floovant.id, form="com", lemma="come1", context="non Cloovis si com truis en escrit", label_uniform="come1", morph="_"),
    WordToken(corpus=Floovant.id, form="truis", lemma="trover", context="Cloovis si com truis en escrit", label_uniform="trover", morph="MODE=ind|TEMPS=pst|PERS.=1|NOMB.=s"),
    WordToken(corpus=Floovant.id, form="en", lemma="en1", context="si com truis en escrit", label_uniform="en1", morph="_"),
    WordToken(corpus=Floovant.id, form="escrit", lemma="escrit", context="com truis en escrit", label_uniform="escrit", morph="NOMB.=s|GENRE=m|CAS=r")

]
FloovantAllowedPOS = [
    AllowedPOS(corpus=Floovant.id, label="ADVgen"),
    AllowedPOS(corpus=Floovant.id, label="VERcjg"),
    AllowedPOS(corpus=Floovant.id, label="NOMcom"),
    AllowedPOS(corpus=Floovant.id, label="ADJord"),
    AllowedPOS(corpus=Floovant.id, label="ADJqua"),
    AllowedPOS(corpus=Floovant.id, label="ADVneg"),
    AllowedPOS(corpus=Floovant.id, label="CONsub"),
    AllowedPOS(corpus=Floovant.id, label="DETcar"),
    AllowedPOS(corpus=Floovant.id, label="NOMpro"),
    AllowedPOS(corpus=Floovant.id, label="PRE"),
    AllowedPOS(corpus=Floovant.id, label="PRE.DETdef"),
    AllowedPOS(corpus=Floovant.id, label="PROdem"),
    AllowedPOS(corpus=Floovant.id, label="PROper"),
    AllowedPOS(corpus=Floovant.id, label="PROrel")
]
FloovantAllowedLemma = [
    AllowedLemma(corpus=Floovant.id, label="escouter", label_uniform="escouter"),
    AllowedLemma(corpus=Floovant.id, label="or4", label_uniform="or4"),
    AllowedLemma(corpus=Floovant.id, label="seignor", label_uniform="seignor"),
    AllowedLemma(corpus=Floovant.id, label="ami", label_uniform="ami"),
    AllowedLemma(corpus=Floovant.id, label="avoir", label_uniform="avoir"),
    AllowedLemma(corpus=Floovant.id, label="bon", label_uniform="bon"),
    AllowedLemma(corpus=Floovant.id, label="cel", label_uniform="cel"),
    AllowedLemma(corpus=Floovant.id, label="clovis", label_uniform="clovis"),
    AllowedLemma(corpus=Floovant.id, label="come1", label_uniform="come1"),
    AllowedLemma(corpus=Floovant.id, label="crestiien", label_uniform="crestiien"),
    AllowedLemma(corpus=Floovant.id, label="de", label_uniform="de"),
    AllowedLemma(corpus=Floovant.id, label="de+le", label_uniform="de+le"),
    AllowedLemma(corpus=Floovant.id, label="devenir", label_uniform="devenir"),
    AllowedLemma(corpus=Floovant.id, label="deviser", label_uniform="deviser"),
    AllowedLemma(corpus=Floovant.id, label="dieu", label_uniform="dieu"),
    AllowedLemma(corpus=Floovant.id, label="en1", label_uniform="en1"),
    AllowedLemma(corpus=Floovant.id, label="escrit", label_uniform="escrit"),
    AllowedLemma(corpus=Floovant.id, label="estoire1", label_uniform="estoire1"),
    AllowedLemma(corpus=Floovant.id, label="estre1", label_uniform="estre1"),
    AllowedLemma(corpus=Floovant.id, label="france", label_uniform="france"),
    AllowedLemma(corpus=Floovant.id, label="il", label_uniform="il"),
    AllowedLemma(corpus=Floovant.id, label="je", label_uniform="je"),
    AllowedLemma(corpus=Floovant.id, label="nom", label_uniform="nom"),
    AllowedLemma(corpus=Floovant.id, label="premier", label_uniform="premier"),
    AllowedLemma(corpus=Floovant.id, label="que4", label_uniform="que4"),
    AllowedLemma(corpus=Floovant.id, label="qui", label_uniform="qui"),
    AllowedLemma(corpus=Floovant.id, label="roi2", label_uniform="roi2"),
    AllowedLemma(corpus=Floovant.id, label="si", label_uniform="si"),
    AllowedLemma(corpus=Floovant.id, label="trois1", label_uniform="trois1"),
    AllowedLemma(corpus=Floovant.id, label="trover", label_uniform="trover"),
    AllowedLemma(corpus=Floovant.id, label="vers1", label_uniform="vers1"),
    AllowedLemma(corpus=Floovant.id, label="vos1", label_uniform="vos1")
]
FloovantAllowedMorph = [
    AllowedMorph(corpus=Floovant.id, label="_", readable="pas de morphologie"),
    AllowedMorph(corpus=Floovant.id, label="DEGRE=-", readable="non applicable"),
    AllowedMorph(corpus=Floovant.id, label="MODE=imp|PERS.=2|NOMB.=p", readable="impératif 2e personne pluriel"),
    AllowedMorph(corpus=Floovant.id, label="MODE=ind|TEMPS=psp|PERS.=3|NOMB.=s", readable="indicatif passé simple 3e personne singulier"),
    AllowedMorph(corpus=Floovant.id, label="MODE=ind|TEMPS=pst|PERS.=1|NOMB.=s", readable="indicatif présent 1re personne singulier"),
    AllowedMorph(corpus=Floovant.id, label="MODE=sub|TEMPS=pst|PERS.=3|NOMB.=s", readable="subjonctif présent 3e personne singulier"),
    AllowedMorph(corpus=Floovant.id, label="NOMB.=p|GENRE=m|CAS=n", readable="pluriel masculin nominatif"),
    AllowedMorph(corpus=Floovant.id, label="NOMB.=p|GENRE=m|CAS=r", readable="pluriel masculin régime"),
    AllowedMorph(corpus=Floovant.id, label="NOMB.=s|GENRE=f|CAS=r", readable="singulier féminin régime"),
    AllowedMorph(corpus=Floovant.id, label="NOMB.=s|GENRE=f|CAS=r|DEGRE=p", readable="singulier féminin régime positif"),
    AllowedMorph(corpus=Floovant.id, label="NOMB.=s|GENRE=m|CAS=n", readable="singulier masculin nominatif"),
    AllowedMorph(corpus=Floovant.id, label="NOMB.=s|GENRE=m|CAS=r", readable="singulier masculin régime"),
    AllowedMorph(corpus=Floovant.id, label="PERS.=1|NOMB.=s|GENRE=m|CAS=n", readable="1re personne singulier masculin nominatif"),
    AllowedMorph(corpus=Floovant.id, label="PERS.=2|NOMB.=p|GENRE=m|CAS=r", readable="2e personne pluriel masculin régime"),
    AllowedMorph(corpus=Floovant.id, label="PERS.=3|NOMB.=p|GENRE=m|CAS=r", readable="3e personne pluriel masculin régime")
]
