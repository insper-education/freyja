# freyja
Coletamos as almas dos repositórios (e dos alunos)

#### Create repo list

```  
    nome base do repositorio |                      | salva lista em
                             v                      v
./getReposList.py --filter 21a-emb-aps2 --save repos-emb-aps2.yml
```

#### Download repos

```
     arquivo com lista dos repos |                         | salva na pasta
                                 v                         v
./downloadRepos.py --config repos-emb-aps2.yml --save emb-aps2
```

#### Create issues 

Cria issues em uma lista de repositórios.

```
./issuesCreate.py --config issues.yml --repos repos-emb-aps2.yml --issues
```

issues.yml

``` yml
issues:
  issue0:
    Title: Primeira issues
    Body: |
      **Conteúdo pode ser em markdown!**

  issues1:
    Title: Segunda issue
    Body: |
      Lembre de:
      
      - [ ] Ler o readme
      - [ ] Ler a rubrica
``` 


