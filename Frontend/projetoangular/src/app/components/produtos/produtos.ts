import { Component, inject } from '@angular/core';
import { Produto } from '../../interfaces/modelo_produto';
import { ProdutoService } from '../../services/produto.service';

@Component({
  selector: 'app-produtos',
  imports: [],
  templateUrl: './produtos.html',
  styleUrl: './produtos.scss',
  standalone: true,
})
export class Produtos {
  private produtoService: ProdutoService = inject(ProdutoService);

  lprodutos: Produto[] = [];
  ngOnInit(): void {
    this.lprodutos = this.produtoService.getProdutos();
  }

}
