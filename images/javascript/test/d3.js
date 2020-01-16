    d3.csv("./romance.csv", function(data){
    var width = 1000;
    var height = 1000;
    var radius = Math.min(width, height) / 2;
    var donutWidth = 300;                            // NEW

    var lastR = 0;
    var lastG = 0;
    var lastB = 0;

    var svg = d3.select('#graph')
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .append('g')
      .attr('transform', 'translate(' + (width / 2) + 
        ',' + (height / 2) + ')');

    var arc = d3.arc()
      .innerRadius(radius - donutWidth)             // NEW
      .outerRadius(radius);
      
    var pie = d3.pie()
      .value(function(d) { return 1/3441; })
      .sort(null);
      
    var path = svg.selectAll('path')
      .data(pie(data))
      .enter()
      .append('path')
      .attr('d', arc)
      .attr('stroke-width', '0')
      .attr('stroke', 'none')
      .attr('fill', function(d){
        if(Math.abs(d.data.R - lastR) > 20 || Math.abs(d.data.G - lastG) > 20 || Math.abs(d.data.B - lastB) > 20){
          lastR = d.data.R;
          lastG = d.data.G;
          lastB = d.data.B;
        }
        return "rgb(" + lastR + "," + lastG + "," + lastB + ")"});

  })