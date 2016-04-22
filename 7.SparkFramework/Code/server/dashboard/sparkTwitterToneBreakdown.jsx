import React, { Component, PropTypes } from 'react';
import reactMixin                      from 'react-mixin';
import Mozaik                          from 'mozaik/browser';
import { ListenerMixin }               from 'reflux';
import c3                              from 'c3';
import _                               from 'lodash';

class SparkTwitterToneBreakdown extends Component{
	constructor(props) {
        super(props);
        
        this.state = {
    		"colData": []
    	};
    }

    getApiRequest() {
    	//console.log("Calling getApiRquest for tone widget");
        return {
            id: 'sparkTwitter.getToneBreakdown',
            params: {
            	topic: "topHashTags.toneScores"
            }
        };
    }

    onApiData(metrics) {
        this.setState({"colData":metrics});
    }

    componentDidUpdate() {
    	if ( this.state.colData.length > 0 ) {
    	    console.log(this.chart);
    	    var d = this.getChartData();
    		this.chart.load(d);
    		//this.chart.groups = [_.flatMap(_.tail(d.columns), function(item) {return _.head(item); })];
    		this.onResize();
    	}
    }
    
    getChartData(){
    	var retData = {"columns": this.state.colData, "unload":[]};

    	//Unload any columns that is not part of the colData
    	var data = retData.columns;
    	_.forEach( this.chart.data(), function(t){
    		if ( !_.find(data, function(u){
    			return u[0]===t.id;
    		})){
    			retData.unload.push(t.id);
    		}
    	});

    	var res = [];
        _.each(retData.columns, function(item) {
          _.each(_.tail(item), function(elem, idx) {
            if (res[idx] !== undefined) {
              res[idx] = res[idx] + elem;
            } else {
              res[idx] = 0;
            }
          });
        });

        var items = [_.head(retData.columns)].concat([["Totals"].concat(res)]);

        console.log(items);

    	retData.columns = items;
    	
    	return retData;
    }
    
    onResize() {
    	if (this.chart) {
    		var parent = document.querySelector(".sparkTwitter-toneBreakDown-chart").parentNode;
    		this.chart.resize({ height: parent.offsetHeight - 50 });
    	}
    }

    componentDidMount() {
      var chartElement = React.findDOMNode(this.refs.chartWrapper);
      this.chart = c3.generate({
    	  bindto: chartElement,
    	  data: {
    		  x:'x',
    		  columns: this.state.colData,
    		  type : 'bar'
    	  },
    	  bar: {
			width: {
			    ratio: 0.5 // this makes bar width 50% of length between ticks
			}
    	  },
    	  axis: {
	        x : {
	            type:'categorized'
	        }
    	  }
      });

      window.addEventListener('resize', this.onResize.bind(this));
      this.onResize();
    }

    componentWillUnmount() {
      window.removeEventListener('resize', this.onResize.bind(this));
      if (this.chart) {
        this.chart.destroy();
      }
    }

    render() {
    	return (
    		<div style={{height:'100%'}}>
	    		<div className="chart-title-text">World Emotions</div>
	            <div ref="chartWrapper" className="sparkTwitter-toneBreakDown-chart"></div>
	        </div>
        );
  	}
}

reactMixin(SparkTwitterToneBreakdown.prototype, ListenerMixin);
reactMixin(SparkTwitterToneBreakdown.prototype, Mozaik.Mixin.ApiConsumer);
export { SparkTwitterToneBreakdown as default };
