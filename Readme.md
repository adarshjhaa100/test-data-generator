<h1> Test Data Generator </h1>
<p>
   Application for generationg test data according to provided column configurations like:
   <ul>
   <li>Name</li>
   <li>Max Length</li>
   <li>Range</li>
   <li>Variance etc.</li>
   </ul>  

   <b>Progress:</b> Completed logic to generate simple columns(string, float, int) separately. 
   <br/> 
   Goto "docs/workflow_design.txt" for the workflow design and column configuration information.
   <br/>
   To generate columns, do the following:
   <ol>
   <li> Switch directory to generatorLogicScripts using: </br><code>cd generatorLogicScripts</code></li>
   <l1> Add column config to 'sampleconfigs\simpleconfig1.json' according to config information present in "docs/workflow_design.txt"</li>
   <l1> Create a folder named sampleoutput inside generatorLogicScripts </li>
   <l1> Modify the NUM_ROWS variable in generatesimplecol.py with the number of rows requried </li>
   <l1> Run the file generatesimplecol.py using <br/> <code> python generatesimplecol.py</code> </li>
   </ol>

   In case requirement do not match, user can pass a custom script to generate the specific column, it will be saved as a python file in the **/col_scripts directory.  
</p>

