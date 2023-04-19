import { AfterViewInit, Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-graphs',
  templateUrl: './graphs.component.html',
  styleUrls: ['./graphs.component.css']
})
export class GraphsComponent implements AfterViewInit{
  chart: any;
  dataPoints: any = [];
  showChart: Boolean = false;

  constructor(private http: HttpClient) { }

  chartOptions = {
    animationEnabled: true,
    theme: 'light1', //"light2", "dark1", "dark2"
    title: {
      text: 'Enery over Time',
    },
    axisX: {
      title: 'Time(Hours)',
      reversed: false,
    },
    axisY: {
      title: 'Volts',
      includeZero: true,
    },
    data: [
      {
        type: "line",
        dataPoints: this.dataPoints,
      },
    ],
  };
  getChartInstance(chart: object) {
    this.chart = chart;
  }

  ngAfterViewInit() {
    this.http
      .get('/assets/sample.csv', {
        responseType: 'text',
      })
      .subscribe((response: any) => {
        let csvRowData = response.split(/[\r?\n|\r|\n]+/);
        csvRowData.forEach((rowData: any, index: number) => {
          if (index === 0) return;
          var data = rowData.split(',');
          this.dataPoints.push({ label: data[0], y: parseInt(data[1]) });
        });
        this.showChart = true;
      });
  }
}
