import { Routes } from '@angular/router';
import { ComponenteInicial } from './components/componente-inicial/componente-inicial';
import { Produtos } from './components/produtos/produtos';
import { TarefaComponent } from './components/tarefas/tarefas';


export const routes: Routes = [
    { path: '', component: ComponenteInicial },
    { path: 'produtos', component: Produtos },
    { path: 'tarefas', component: TarefaComponent },
    { path: '**', redirectTo: '' }
];

