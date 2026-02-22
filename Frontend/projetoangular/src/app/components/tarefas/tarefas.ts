import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Tarefa } from '../../interfaces/inteface_Tarefa';
import { TarefaService } from '../../services/tarefa.service';


@Component({
  selector: 'app-tarefa',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './tarefa.html',
  styleUrl: './tarefa.scss'
})
export class TarefaComponent implements OnInit {

  private tarefaService: TarefaService = inject(TarefaService);

  listaTarefas: Tarefa[] = [];

  ngOnInit(): void {
    this.listaTarefas = this.tarefaService.getTarefas();
  }

  toggleConcluido(tarefa: Tarefa): void {
    tarefa.concluido = !tarefa.concluido;
  }

}
