import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-componente-inicial',
  imports: [FormsModule],
  templateUrl: './componente-inicial.html',
  standalone: true,
  styleUrl: './componente-inicial.scss',
})
export class ComponenteInicial {
  nome: string = 'Michelle souza';
  profissao: string = 'Desenvolvedor';
  hobbies: string[] = ['ler', 'estudar', 'programar'];
  idade: number = 25;
  ativo: boolean = true;
  url_da_imagem: string = 'https://avatars.githubusercontent.com/u/65325858?v=4';

  mudarNome(): void {
    this.nome = 'Novo Nome';
  }
  alterarStatus(): void {
    this.ativo = !this.ativo;
  }
  adicionarHobby(novoHobby: string): void {
    this.hobbies.push(novoHobby);
  }
}