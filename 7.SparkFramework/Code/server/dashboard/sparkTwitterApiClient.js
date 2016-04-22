'use strict';

/**
 * Dashboard for Twitter Sentiment analysis using Spark Streaming and Watson Tone Analyzer
 *
 * @author David Taieb ,  Edit by Afnan Aldhahri
 */

var request = require('superagent');
require('superagent-bluebird-promise');
var messageHubBridge = require('../messageHubBridge');

var client = function (mozaik) {
    return {
    	runInterval: 5000,
        getTopHashTags: function(params) {
            return new Promise( function( resolve, reject){
            		resolve();
            	})
                .then(function (res) {
                	//console.log("Calling Api with params: ", params);
                	return messageHubBridge.getTopicMessage(params.topic);
                });
        },
        getToneBreakdown:function(params) {
            return new Promise( function( resolve, reject){
            		resolve();
            	})
                .then(function (res) {
                	//console.log("Calling Api with params: ", params);
                	return messageHubBridge.getTopicMessage(params.topic);
                });
        }
    };
};

module.exports = client;
