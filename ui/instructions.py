instructions_text = """
        <h1>Application Instructions</h1>
        <p>Welcome to the Plot Function App!</p>

        <ol>
            <li><strong>Enter a Function</strong>: Type your function in the "Function" section (e.g., <code>x^2 + sin(x)</code>).</li>
            <li><strong>Supported functions:</strong> 
                <ul>
                    <li>All operators <code>+ - / * ^</code></li>
                    <li>All trigonometric functions <code>sin(x), cos(x), tan(x)</code>, etc...</li>
                    <li>Square root function <code>sqrt(x)</code></li>
                    <li>Log functions <code>log(x), log10(x), log2(x)</code></li>
                    <li>Symbols: pi as <code>pi</code> and e<sup>x</sup> as <code>exp(x)</code></li>
                </ul>
            </li>
            <li><strong>Specify X Range</strong>: 
                <ul>
                    <li><strong>X Min</strong>: Minimum x value.</li>
                    <li><strong>X Max</strong>: Maximum x value.</li>
                    <li><strong>Note:</strong> The maximum value <strong>must</strong> be greater than the minimum value.</li>
                </ul>
            </li>
            <li><strong>Set the Step Size</strong>: Interval between plotted points (e.g., <code>0.1</code>).</li>
            <li><strong>Plot</strong>: Click "Plot" to generate the graph.</li>
            <li><strong>Clear</strong>: Click "Clear" to remove the plot and reset the area.</li>
            <li><strong>Instructions</strong>: Click "Instructions" to see these guidelines again.</li>
        </ol>

        <h2>Example</h2>
        <p>To plot <code>x^2</code> from <code>-10</code> to <code>10</code> with a step of <code>0.5</code>, enter these values and click "Plot".</p>

        <h2>Need Help?</h2>
        <p>Refer to error messages for guidance or go to <a href="https://github.com/xSkkarf/Math-function-plotter-GUI">Github repository</a></p>

        """