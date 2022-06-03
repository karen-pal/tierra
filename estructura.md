# Pensando relacion tierras <-> qué mostrar

cielo_estrellado/
cielo_galaxias/
flor_cielo_noche/


en estas tierras tenemos

S: 
cielo
estrella
galaxia
noche
flor

V:
despierta
florece


"la noche se enciende" -> cielo_estrellado ? cielo_florece? cielo_galaxia?
"despierta la chacarera"

# Posibles sintaxis

## como lenguaje natural

▮ florece la noche.

▮ florece la noche

▮ despierta la chacarera

▮ tiene un misterio escondido
## JS like
▮ noche.florece()

▮ noche.con(nube).florece()


▮ chacarera.despierta()

▮ misterio.es(escondido).tiene()

## python like

▮ florece(noche)
▮ florece(noche, nube)

▮ despierta(chacarera)

▮ tiene(misterio, escondido)

## lisp like
▮ ( florece (noche) (estrella) )
▮ ( florece (noche) (nube) )

▮ ( tiene (misterio) (escondido) )

## Prolog like?

▮ florece:- noche  
▮ estrella,noche:- florece

# Estructura
tierras/

index.html <- tomar input + hacer post post

server.py <- post retornar tierras/path



# Links

[dataflow programming](https://en.wikipedia.org/wiki/Dataflow_programming)
[Cognitive dimensions of notations](https://en.wikipedia.org/wiki/Cognitive_dimensions_of_notations)


# Idea

Hay que definir el vocabulario primero, eso me doy cuenta.

y si hubiera una tabla que relacione numericamente palabras con prompts?





