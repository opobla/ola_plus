(function() {
    const search = instantsearch({
        searchClient: algoliasearch('DW2KOJ8AHI', 'af75e889b6ff2e8a18533f0ee8fb8342'),
        indexName: 'pushdata',
        routing: true
    });

    search.addWidget(
        instantsearch.widgets.searchBox({
            container: '#searchbox',
        })
    );

    search.addWidget(
        instantsearch.widgets.clearRefinements({
            container: '#clear-refinements',
        })
    );

    search.addWidget(
        instantsearch.widgets.refinementList({
            container: '#des_plan',
            attribute: 'des_plan',
        })
    );
    search.addWidget(
        instantsearch.widgets.refinementList({
            container: '#hei',
            attribute: 'hei',
        })
    );

    search.addWidget(
        instantsearch.widgets.hits({
            container: '#hits',
            templates: {
                item: `
        <div>
          <img src="{{image}}" align="left" alt="{{name}}" />
          <div class="hit-name">
            {{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}
          </div>
          <div class="hit-description">
            {{#helpers.highlight}}{ "attribute": "des_plan" }{{/helpers.highlight}}
          </div>
          <div class="hit-price">\ECTS {{credit_value}}</div>
        </div>
      `,
            }
        })
    );

    search.addWidget(
        instantsearch.widgets.pagination({
            container: '#pagination',
        })
    );

    search.start();

})();
