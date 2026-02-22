import { Injectable } from '@angular/core';
import { Produto } from '../interfaces/modelo_produto';

@Injectable({
  providedIn: 'root',
})
export class ProdutoService {
  getProdutos(): Produto[] {
    return [
      { nome: 'Notebook', promocao: true, preco: 9000 },
      { nome: 'Mouse', promocao: false, preco: 87 },
      { nome: 'Monitor', promocao: false, preco: 999 },
      { nome: 'TV', promocao: true, preco: 2400 },
      { nome: 'Teclado', promocao: false, preco: 355 },
    ];
  }
}
