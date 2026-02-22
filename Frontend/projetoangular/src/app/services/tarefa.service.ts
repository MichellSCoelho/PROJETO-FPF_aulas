import { Injectable } from '@angular/core';
import { Tarefa } from '../interfaces/inteface_Tarefa';

@Injectable({
  providedIn: 'root'
})
export class TarefaService {

  constructor() { }

  getTarefas(): Tarefa[] {
    return [
      {
        titulo: 'Estudar Angular',
        descricao: 'Revisar componentes e serviços',
        concluido: false
      },
      {
        titulo: 'Fazer exercício',
        descricao: 'Lista dinâmica',
        concluido: true
      },
      {
        titulo: 'Treinar TypeScript',
        descricao: 'Praticar tipagem',
        concluido: false
      }
    ];
  }
}