import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.scss']
})
export class SearchbarComponent implements OnInit {

  private searchTerm: string = '';
  private maxSearchLength = 100;

  constructor() { }

  ngOnInit() {
  }

  onSearchTermChange(event) {
    console.log('term is ' + this.searchTerm);
  }

}
