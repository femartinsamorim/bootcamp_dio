programa {
	funcao inicio() {
	    real a,b,c,d
	    escreva ("Digite a notas PROVA1 e PROVA2 do aluno A: ")
	    leia (a)
	    leia (b)
	    escreva ("Digite a notas PROVA1 e PROVA2 do aluno B ")
	    leia (c)
	    leia (d)
	    
	    escreva ("Média do aluno A : ", media_aluno(a,b))
	    escreva ("\nMédia do aluno B : ", media_aluno(c,d))
		
	}
	funcao real media_aluno(real a, real b){
	    retorne (a + b)/2
	}
}
