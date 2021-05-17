# freyja
Coletamos as almas dos repositórios (e dos alunos)

## Req.

Para usar os scripts você deve:

1. Instalar o GitHub CLI (gh) seguindo os passos em: https://github.com/cli/cli
2. Autenticar com o gh: `gh auth login` 

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
./downloadRepos.py --repos repos-emb-aps2.yml --save emb-aps2
```

#### Create issues 

Cria issues em uma lista de repositórios.

```
./createIssues.py --repos repos-emb-aps2.yml --issues issues.yml
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
#### pull local reps

Pull new changes from local repositories with upstream 

```
		            | folder with repositories		
                            v
./pullLocalReps.py --path emb-aps
```

