// Load environment variables from .env file if available
require('dotenv').load();

var config = {
    env:  'prod',

    host: 'localhost',
    port: process.env.PORT || 8081,

    theme: 'analytics',

    //For letting gulp task know where to build from
    src: 'server/dashboard',

    // clients configs
    api: {
    },

    // define duration between each dashboard rotation (ms)
    rotationDuration: 4000,

    dashboards: [
        {
            columns: 5, rows: 100,
            widgets: [
                {
                    type: 'sparkTwitter.tone_breakdown',
                    columns: 3, rows: 45,
                    x: 1, y: 15
                }
            ]
        }
    ]
};

module.exports = config;
