define([
        'raven',
        ], function(Raven) {

    Raven.config([
            'https://8be3d66e72604e20bb74712f39926d69:',
            '186dc82c9a4749129a9b9652cde82390@',
            'app.getsentry.com/4320',
            ].join('')).install();

    errorHandler = function(error) {
        Raven.captureException(error);
        alert([
                'Houston we\'ve had a problem.',
                'We\'ve had a MAIN B BUS UNDERVOLT.',
                'Roger. MAIN B UNDERVOLT.',
                'Okay, stand by, 13. We\'re looking at it.',
                ].join('\n'));
        throw error;
    };

    return {errorHandler: errorHandler};
});
