listaestados = {
		"SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53}
total = (sum((listaestados.values())))
print("Percentual de SP:",(listaestados["SP"])/total*100,"%")
print("Percentual de RJ:",(listaestados["RJ"])/total*100,"%")
print("Percentual de MG:",(listaestados["MG"])/total*100,"%")
print("Percentual de ES:",(listaestados["ES"])/total*100,"%")
print("Percentual dos outros:",(listaestados["Outros"])/total*100,"%")