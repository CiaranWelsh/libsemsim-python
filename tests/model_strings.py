teusnik2000 = """<?xml version='1.0' encoding='UTF-8' standalone='no'?>
<!-- This model was downloaded from BioModels Database -->
<!-- http://www.ebi.ac.uk/biomodels-static/                   -->
<!-- Wed Feb 12 20:37:12 GMT 2020                      -->
<sbml xmlns="http://www.sbml.org/sbml/level2" level="2" metaid="metaid_0000001" version="1">
    <model id="Teusink2000_Glycolysis" metaid="metaid_0000002" name="Teusink2000_Glycolysis">
        <notes>
            <body xmlns="http://www.w3.org/1999/xhtml">
                <p>
                    <b>Can yeast glycolysis be understood in terms of in vitro kinetics of the constituent enzymes?
                        Testing biochemistry.
                    </b>
                    <br/>
                    <i>Teusink,B et al.: Eur J Biochem 2000 Sep;267(17):5313-29.</i>
                    <br/>
                    The model reproduces the steady-state fluxes and metabolite concentrations of the branched model as
                    given in Table 4 of the paper. It is derived from the model on JWS online, but has the ATP
                    consumption in the succinate branch with the same stoichiometrie as in the publication. The model
                    was successfully tested on copasi v.4.4(build 26).
                    <br/>
                    For Vmax values, please note that there is a conversion factor of approx. 270 to convert from
                    U/mg-protein as shown in Table 1 of the paper to mmol/(min*L_cytosol). The equilibrium constant for
                    the ADH reaction in the paper is given for the reverse reaction (Keq = 1.45*10      <sup>4</sup>          ).
                    The value used in this model is for the forward reaction: 1/Keq = 6.9*10      <sup>-5</sup>          .
                    <br/>
                    Vmax parameters values used (in [mM/min] except VmGLT):
                    <table border="0" cellpadding="2" cellspacing="0">
                        <tr>
                            <td>
                                <b>VmGLT</b>
                            </td>
                            <td>97.264</td>
                            <td>mmol/min</td>
                        </tr>
                        <tr>
                            <td>
                                <b>VmGLK</b>
                            </td>
                            <td>226.45</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmPGI</b>
                            </td>
                            <td>339.667</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmPFK</b>
                            </td>
                            <td>182.903</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmALD</b>
                            </td>
                            <td>322.258</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmGAPDH_f</b>
                            </td>
                            <td>1184.52</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmGAPDH_r</b>
                            </td>
                            <td>6549.68</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmPGK</b>
                            </td>
                            <td>1306.45</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmPGM</b>
                            </td>
                            <td>2525.81</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmENO</b>
                            </td>
                            <td>365.806</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmPYK</b>
                            </td>
                            <td>1088.71</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmPDC</b>
                            </td>
                            <td>174.194</td>
                            <td/>
                        </tr>
                        <tr>
                            <td>
                                <b>VmG3PDH</b>
                            </td>
                            <td>70.15</td>
                            <td/>
                        </tr>
                    </table>
                    The result of the G6P steady state concentration (marked in red) differs slightly from the one given
                    in table 4. of the publication
                    <br/>
                    Results for steady state:
                    <table border="0" cellpadding="2" cellspacing="0">
                        <thead>
                            <tr>
                                <th align="left" bgcolor="#eeeeee" valign="middle"/>
                                <th align="left" bgcolor="#eeeeee" valign="middle">orig. article</th>
                                <th align="center" bgcolor="#eeeeee" valign="middle">this model</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <b>Fluxes[mM/min]</b>                   
                                </td>
                                <td/>
                                <td/>
                            </tr>
                            <tr>
                                <td>Glucose </td>
                                <td>88 </td>
                                <td>88 </td>
                            </tr>
                            <tr>
                                <td>Ethanol </td>
                                <td>129 </td>
                                <td>129 </td>
                            </tr>
                            <tr>
                                <td>Glycogen </td>
                                <td>6 </td>
                                <td>6 </td>
                            </tr>
                            <tr>
                                <td>Trehalose </td>
                                <td>4.8 </td>
                                <td>4.8 </td>
                                <td>(G6P flux through trehalose branch)</td>
                            </tr>
                            <tr>
                                <td>Glycerol </td>
                                <td>18.2 </td>
                                <td>18.2 </td>
                            </tr>
                            <tr>
                                <td>Succinate </td>
                                <td>3.6 </td>
                                <td>3.6 </td>
                            </tr>
                            <tr>
                                <td>
                                    <b>Conc.[mM]</b>                   
                                </td>
                                <td/>
                                <td/>
                            </tr>
                            <tr>
                                <td>G6P </td>
                                <td>1.07 </td>
                                <td style="color: red">1.03 </td>
                            </tr>
                            <tr>
                                <td>F6P </td>
                                <td>0.11 </td>
                                <td>0.11 </td>
                            </tr>
                            <tr>
                                <td>F1,6P </td>
                                <td>0.6 </td>
                                <td>0.6 </td>
                            </tr>
                            <tr>
                                <td>DHAP </td>
                                <td>0.74 </td>
                                <td>0.74 </td>
                            </tr>
                            <tr>
                                <td>3PGA </td>
                                <td>0.36 </td>
                                <td>0.36 </td>
                            </tr>
                            <tr>
                                <td>2PGA </td>
                                <td>0.04 </td>
                                <td>0.04 </td>
                            </tr>
                            <tr>
                                <td>PEP </td>
                                <td>0.07 </td>
                                <td>0.07 </td>
                            </tr>
                            <tr>
                                <td>PYR </td>
                                <td>8.52 </td>
                                <td>8.52 </td>
                            </tr>
                            <tr>
                                <td>AcAld </td>
                                <td>0.17 </td>
                                <td>0.17 </td>
                            </tr>
                            <tr>
                                <td>ATP </td>
                                <td>2.51 </td>
                                <td>2.51 </td>
                            </tr>
                            <tr>
                                <td>ADP </td>
                                <td>1.29 </td>
                                <td>1.29 </td>
                            </tr>
                            <tr>
                                <td>AMP </td>
                                <td>0.3 </td>
                                <td>0.3 </td>
                            </tr>
                            <tr>
                                <td>NAD </td>
                                <td>1.55 </td>
                                <td>1.55 </td>
                            </tr>
                            <tr>
                                <td>NADH </td>
                                <td>0.04 </td>
                                <td>0.04 </td>
                            </tr>
                        </tbody>
                    </table>
                    Authors of the publication also mentioned a few misprints in the original article:
                    <br/>
                    in the kinetic law for      <em>ADH</em>          :
                    <ol>
                        <li>the species          <em>a</em>              should denote          <em>NAD</em>              and          <em>
                            b
                        </em>
                            <em>Ethanol</em>
                        </li>
                        <li>the last term in the equation should read          <em>bpq</em>              /(
                            <em>K            <sub>ib</sub>                K            <sub>iq</sub>                K            <sub>
                                p
                            </sub>
                            </em>
                            )
                        </li>
                    </ol>
                    in the kinetic law for      <em>PFK</em>          :
                    <ol>
                        <li>R = 1 + λ          <sub>1</sub>              + λ          <sub>2</sub>              + g          <sub>
                            r
                        </sub>              λ          <sub>1</sub>              λ
                            <sub>2</sub>
                        </li>
                        <li>equation L should read: L = L0*(..)          <sup>2</sup>              *(..)          <sup>
                            2
                        </sup>              *(..)          <sup>2</sup>              not L = L0*(..)          <sup>2
                        </sup>              *(..)          <sup>2</sup>              *(..)
                        </li>
                    </ol>
                    To make the model easier to curate, the species      <em>ATP</em>          ,      <em>ADP</em>          and      <em>
                    AMP
                </em>          were added. These are calculated via assignment rules from the active phosphate species,      <em>
                    P
                </em>          , and the sum of all      <em>AXP</em>          ,      <em>SUM_P</em>          .
                </p>
                <br/>
                <p>To the extent possible under law, all copyright and related or neighbouring rights to this encoded
                    model have been dedicated to the public domain worldwide. Please refer to      <a
                            href="http://creativecommons.org/publicdomain/zero/1.0/" title="Creative Commons CC0">CC0
                        Public Domain Dedication
                    </a>          for more information.
                </p>
                <p>In summary, you are entitled to use this encoded model in absolutely any manner you deem suitable,
                    verbatim, or with modification, alone or embedded it in a larger context, redistribute it,
                    commercially or not, in a restricted way or not.
                </p>
                <br/>
                <p>To cite BioModels Database, please use:
                    <a href="http://www.ncbi.nlm.nih.gov/pubmed/20587024" target="_blank">Li C, Donizelli M, Rodriguez
                        N, Dharuri H, Endler L, Chelliah V, Li L, He E, Henry A, Stefan MI, Snoep JL, Hucka M, Le Novère
                        N, Laibe C (2010) BioModels Database: An enhanced, curated and annotated resource for published
                        quantitative kinetic models. BMC Syst Biol., 4:92.
                    </a>
                </p>
            </body>
        </notes>
        <annotation>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                     xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                     xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:dc="http://purl.org/dc/elements/1.1/"
                     xmlns:dcterms="http://purl.org/dc/terms/" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                <rdf:Description rdf:about="#metaid_0000002">
                    <dc:creator>
                        <rdf:Bag>
                            <rdf:li rdf:parseType="Resource">
                                <vCard:N rdf:parseType="Resource">
                                    <vCard:Family>Snoep</vCard:Family>
                                    <vCard:Given>Jacky L</vCard:Given>
                                </vCard:N>
                                <vCard:EMAIL>jls@sun.ac.za</vCard:EMAIL>
                                <vCard:ORG rdf:parseType="Resource">
                                    <vCard:Orgname>Stellenbosh University</vCard:Orgname>
                                </vCard:ORG>
                            </rdf:li>
                            <rdf:li rdf:parseType="Resource">
                                <vCard:N rdf:parseType="Resource">
                                    <vCard:Family>Endler</vCard:Family>
                                    <vCard:Given>Lukas</vCard:Given>
                                </vCard:N>
                                <vCard:EMAIL>lukas@ebi.ac.uk</vCard:EMAIL>
                                <vCard:ORG rdf:parseType="Resource">
                                    <vCard:Orgname>EMBL-EBI</vCard:Orgname>
                                </vCard:ORG>
                            </rdf:li>
                            <rdf:li rdf:parseType="Resource">
                                <vCard:N rdf:parseType="Resource">
                                    <vCard:Family>Dharuri</vCard:Family>
                                    <vCard:Given>Harish</vCard:Given>
                                </vCard:N>
                                <vCard:EMAIL>hdharuri@cds.caltech.edu</vCard:EMAIL>
                                <vCard:ORG rdf:parseType="Resource">
                                    <vCard:Orgname>California Institute of Technology</vCard:Orgname>
                                </vCard:ORG>
                            </rdf:li>
                        </rdf:Bag>
                    </dc:creator>
                    <dcterms:created rdf:parseType="Resource">
                        <dcterms:W3CDTF>2008-09-16T14:00:06Z</dcterms:W3CDTF>
                    </dcterms:created>
                    <dcterms:modified rdf:parseType="Resource">
                        <dcterms:W3CDTF>2012-07-19T18:26:07Z</dcterms:W3CDTF>
                    </dcterms:modified>
                    <bqmodel:is>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/biomodels.db/MODEL6623915522"/>
                        </rdf:Bag>
                    </bqmodel:is>
                    <bqmodel:is>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/biomodels.db/BIOMD0000000064"/>
                        </rdf:Bag>
                    </bqmodel:is>
                    <bqmodel:isDescribedBy>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/pubmed/10951190"/>
                        </rdf:Bag>
                    </bqmodel:isDescribedBy>
                    <bqbiol:hasTaxon>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/taxonomy/4932"/>
                        </rdf:Bag>
                    </bqbiol:hasTaxon>
                    <bqbiol:is>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/kegg.pathway/sce00010"/>
                            <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0006096"/>
                        </rdf:Bag>
                    </bqbiol:is>
                    <bqbiol:isHomologTo>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_723"/>
                        </rdf:Bag>
                    </bqbiol:isHomologTo>
                </rdf:Description>
            </rdf:RDF>
        </annotation>
        <listOfFunctionDefinitions>
            <functionDefinition id="L_PFK" metaid="metaid_0000073" name="L_PFK">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <lambda>
                        <bvar>
                            <ci>L</ci>
                        </bvar>
                        <bvar>
                            <ci>CiATP</ci>
                        </bvar>
                        <bvar>
                            <ci>KiATP</ci>
                        </bvar>
                        <bvar>
                            <ci>CAMP</ci>
                        </bvar>
                        <bvar>
                            <ci>KAMP</ci>
                        </bvar>
                        <bvar>
                            <ci>CF26BP</ci>
                        </bvar>
                        <bvar>
                            <ci>KF26BP</ci>
                        </bvar>
                        <bvar>
                            <ci>CF16BP</ci>
                        </bvar>
                        <bvar>
                            <ci>KF16BP</ci>
                        </bvar>
                        <bvar>
                            <ci>AT</ci>
                        </bvar>
                        <bvar>
                            <ci>AM</ci>
                        </bvar>
                        <bvar>
                            <ci>F16</ci>
                        </bvar>
                        <bvar>
                            <ci>F26</ci>
                        </bvar>
                        <apply>
                            <times/>
                            <ci>L</ci>
                            <apply>
                                <power/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <plus/>
                                        <cn type="integer">1</cn>
                                        <apply>
                                            <times/>
                                            <ci>CiATP</ci>
                                            <apply>
                                                <divide/>
                                                <ci>AT</ci>
                                                <ci>KiATP</ci>
                                            </apply>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <plus/>
                                        <cn type="integer">1</cn>
                                        <apply>
                                            <divide/>
                                            <ci>AT</ci>
                                            <ci>KiATP</ci>
                                        </apply>
                                    </apply>
                                </apply>
                                <cn type="integer">2</cn>
                            </apply>
                            <apply>
                                <power/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <plus/>
                                        <cn type="integer">1</cn>
                                        <apply>
                                            <times/>
                                            <ci>CAMP</ci>
                                            <apply>
                                                <divide/>
                                                <ci>AM</ci>
                                                <ci>KAMP</ci>
                                            </apply>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <plus/>
                                        <cn type="integer">1</cn>
                                        <apply>
                                            <divide/>
                                            <ci>AM</ci>
                                            <ci>KAMP</ci>
                                        </apply>
                                    </apply>
                                </apply>
                                <cn type="integer">2</cn>
                            </apply>
                            <apply>
                                <power/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <plus/>
                                        <cn type="integer">1</cn>
                                        <apply>
                                            <divide/>
                                            <apply>
                                                <times/>
                                                <ci>CF26BP</ci>
                                                <ci>F26</ci>
                                            </apply>
                                            <ci>KF26BP</ci>
                                        </apply>
                                        <apply>
                                            <divide/>
                                            <apply>
                                                <times/>
                                                <ci>CF16BP</ci>
                                                <ci>F16</ci>
                                            </apply>
                                            <ci>KF16BP</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <plus/>
                                        <cn type="integer">1</cn>
                                        <apply>
                                            <divide/>
                                            <ci>F26</ci>
                                            <ci>KF26BP</ci>
                                        </apply>
                                        <apply>
                                            <divide/>
                                            <ci>F16</ci>
                                            <ci>KF16BP</ci>
                                        </apply>
                                    </apply>
                                </apply>
                                <cn type="integer">2</cn>
                            </apply>
                        </apply>
                    </lambda>
                </math>
            </functionDefinition>
            <functionDefinition id="R_PFK" metaid="metaid_0000074" name="R_PFK">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <lambda>
                        <bvar>
                            <ci>KmF6P</ci>
                        </bvar>
                        <bvar>
                            <ci>KmATP</ci>
                        </bvar>
                        <bvar>
                            <ci>g</ci>
                        </bvar>
                        <bvar>
                            <ci>AT</ci>
                        </bvar>
                        <bvar>
                            <ci>F6</ci>
                        </bvar>
                        <apply>
                            <plus/>
                            <cn type="integer">1</cn>
                            <apply>
                                <divide/>
                                <ci>F6</ci>
                                <ci>KmF6P</ci>
                            </apply>
                            <apply>
                                <divide/>
                                <ci>AT</ci>
                                <ci>KmATP</ci>
                            </apply>
                            <apply>
                                <times/>
                                <ci>g</ci>
                                <apply>
                                    <divide/>
                                    <ci>F6</ci>
                                    <ci>KmF6P</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <ci>AT</ci>
                                    <ci>KmATP</ci>
                                </apply>
                            </apply>
                        </apply>
                    </lambda>
                </math>
            </functionDefinition>
            <functionDefinition id="T_PFK" metaid="metaid_0000180" name="T_PFK">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <lambda>
                        <bvar>
                            <ci>CATP</ci>
                        </bvar>
                        <bvar>
                            <ci>KmATP</ci>
                        </bvar>
                        <bvar>
                            <ci>AT</ci>
                        </bvar>
                        <apply>
                            <plus/>
                            <cn type="integer">1</cn>
                            <apply>
                                <times/>
                                <ci>CATP</ci>
                                <apply>
                                    <divide/>
                                    <ci>AT</ci>
                                    <ci>KmATP</ci>
                                </apply>
                            </apply>
                        </apply>
                    </lambda>
                </math>
            </functionDefinition>
        </listOfFunctionDefinitions>
        <listOfUnitDefinitions>
            <unitDefinition id="substance" metaid="metaid_0000070" name="millimole">
                <listOfUnits>
                    <unit kind="mole" metaid="_772471" scale="-3"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="time" metaid="metaid_0000071" name="minute">
                <listOfUnits>
                    <unit kind="second" metaid="_772483" multiplier="60"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="mM" metaid="metaid_0000072" name="mM">
                <listOfUnits>
                    <unit kind="mole" metaid="_772495" scale="-3"/>
                    <unit exponent="-1" kind="litre" metaid="_772507"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="mMpermin" metaid="metaid_0000084" name="mMpermin">
                <listOfUnits>
                    <unit kind="mole" metaid="_772519" scale="-3"/>
                    <unit exponent="-1" kind="litre" metaid="_772531"/>
                    <unit exponent="-1" kind="second" metaid="_772544" multiplier="60"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="permin" metaid="metaid_0000085" name="permin">
                <listOfUnits>
                    <unit exponent="-1" kind="second" metaid="_772557" multiplier="60"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="mmolepermin" metaid="metaid_0000086" name="mmolepermin">
                <listOfUnits>
                    <unit kind="mole" metaid="_772570" scale="-3"/>
                    <unit exponent="-1" kind="second" metaid="_772583" multiplier="60"/>
                </listOfUnits>
            </unitDefinition>
        </listOfUnitDefinitions>
        <listOfCompartments>
            <compartment id="extracellular" metaid="metaid_0000003" size="1">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000003">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0005576"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </compartment>
            <compartment id="cytosol" metaid="metaid_0000075" outside="extracellular" size="1">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000075">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0005829"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </compartment>
        </listOfCompartments>
        <listOfSpecies>
            <species compartment="cytosol" id="GLCi" initialConcentration="0.087" metaid="metaid_0000004"
                     name="Glucose in Cytosol">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000004">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:17234"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00293"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="G6P" initialConcentration="2.45" metaid="metaid_0000005"
                     name="Glucose 6 Phosphate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000005">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:17665"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00668"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="F6P" initialConcentration="0.62" metaid="metaid_0000006"
                     name="Fructose 6 Phosphate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000006">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:15946"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C05345"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="F16P" initialConcentration="5.51" metaid="metaid_0000007"
                     name="Fructose-1,6 bisphosphate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000007">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16905"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00354"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="TRIO" initialConcentration="0.96" metaid="metaid_0000008"
                     name="Triose-phosphate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"
                             xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000008">
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16108"/>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:29052"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00118"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00111"/>
                                    <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:29052"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="BPG" initialConcentration="0" metaid="metaid_0000009"
                     name="1,3-bisphosphoglycerate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000009">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16001"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00236"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="P3G" initialConcentration="0.9" metaid="metaid_0000010"
                     name="3-phosphoglycerate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000010">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:17794"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00197"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="P2G" initialConcentration="0.12" metaid="metaid_0000011"
                     name="2-phosphoglycerate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000011">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:17835"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00631"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="PEP" initialConcentration="0.07" metaid="metaid_0000012"
                     name="Phosphoenolpyruvate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"
                             xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000012">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00074"/>
                                    <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:18021"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:18021"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="PYR" initialConcentration="1.85" metaid="metaid_0000013" name="Pyruvate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"
                             xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000013">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:15361"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00022"/>
                                    <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:32816"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="ACE" initialConcentration="0.17" metaid="metaid_0000014"
                     name="Acetaldehyde">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000014">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:15343"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00084"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="P" initialConcentration="6.31" metaid="metaid_0000042"
                     name="High energy phosphates">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"
                             xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000042">
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00008"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00002"/>
                                    <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16761"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16761"/>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:15422"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="NAD" initialConcentration="1.2" metaid="metaid_0000016" name="NAD">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000016">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:15846"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00003"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="NADH" initialConcentration="0.39" metaid="metaid_0000017" name="NADH">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000017">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16908"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00004"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="cytosol" id="Glyc" initialConcentration="0"
                     metaid="metaid_0000018" name="Glycogen">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000018">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:28087"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00182"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="cytosol" id="Trh" initialConcentration="0"
                     metaid="metaid_0000019" name="Trehalose">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000019">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:27082"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C01083"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="cytosol" id="CO2" initialConcentration="1"
                     metaid="metaid_0000020" name="CO2">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000020">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16526"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00011"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="cytosol" id="SUCC" initialConcentration="0"
                     metaid="metaid_0000021" name="Succinate">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000021">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:30031"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="extracellular" id="GLCo" initialConcentration="50"
                     metaid="metaid_0000022" name="Extracellular Glucose">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000022">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:17234"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00293"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="cytosol" id="ETOH" initialConcentration="50"
                     metaid="metaid_0000023" name="Ethanol">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000023">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16236"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00469"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="cytosol" id="GLY" initialConcentration="0.15"
                     metaid="metaid_0000024" name="Glycerol">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000024">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:17754"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00116"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="ATP" metaid="metaid_0000076" name="ATP concentration">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000076">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:15422"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00002"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="ADP" metaid="metaid_0000077" name="ADP concentration">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000077">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16761"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00008"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="AMP" metaid="metaid_0000078" name="AMP concentration">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000078">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16027"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00020"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" constant="true" id="SUM_P" initialConcentration="4.1" metaid="metaid_0000079"
                     name="sum of AXP conc">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"
                             xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000079">
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:15422"/>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16761"/>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:16027"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00002"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00008"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00020"/>
                                    <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:15422"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" constant="true" id="F26BP" initialConcentration="0.02"
                     metaid="metaid_0000061" name="F2,6P">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000061">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.chebi/CHEBI:28602"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00665"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
        </listOfSpecies>
        <listOfParameters>
            <parameter id="gR" metaid="metaid_0000050" units="dimensionless" value="5.12"/>
            <parameter id="KmPFKF6P" metaid="metaid_0000051" units="mM" value="0.1"/>
            <parameter id="KmPFKATP" metaid="metaid_0000054" units="mM" value="0.71"/>
            <parameter id="Lzero" metaid="metaid_0000055" units="dimensionless" value="0.66"/>
            <parameter id="CiPFKATP" metaid="metaid_0000056" units="dimensionless" value="100"/>
            <parameter id="KiPFKATP" metaid="metaid_0000057" units="mM" value="0.65"/>
            <parameter id="CPFKAMP" metaid="metaid_0000058" units="dimensionless" value="0.0845"/>
            <parameter id="KPFKAMP" metaid="metaid_0000059" units="mM" value="0.0995"/>
            <parameter id="CPFKF26BP" metaid="metaid_0000060" units="dimensionless" value="0.0174"/>
            <parameter id="KPFKF26BP" metaid="metaid_0000062" units="mM" value="0.000682"/>
            <parameter id="CPFKF16BP" metaid="metaid_0000063" units="dimensionless" value="0.397"/>
            <parameter id="KPFKF16BP" metaid="metaid_0000064" units="mM" value="0.111"/>
            <parameter id="CPFKATP" metaid="metaid_0000065" units="dimensionless" value="3"/>
            <parameter id="KeqAK" metaid="metaid_0000080" name="AK eq constant" units="dimensionless" value="0.45"/>
            <parameter id="KeqTPI" metaid="metaid_0000090" name="TPI eq constant" units="dimensionless" value="0.045"/>
        </listOfParameters>
        <listOfRules>
            <assignmentRule metaid="metaid_0000081" variable="ADP">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <apply>
                        <divide/>
                        <apply>
                            <minus/>
                            <ci>SUM_P</ci>
                            <apply>
                                <power/>
                                <apply>
                                    <plus/>
                                    <apply>
                                        <times/>
                                        <apply>
                                            <power/>
                                            <ci>P</ci>
                                            <cn type="integer">2</cn>
                                        </apply>
                                        <apply>
                                            <minus/>
                                            <cn type="integer">1</cn>
                                            <apply>
                                                <times/>
                                                <cn type="integer">4</cn>
                                                <ci>KeqAK</ci>
                                            </apply>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <cn type="integer">2</cn>
                                        <ci>SUM_P</ci>
                                        <ci>P</ci>
                                        <apply>
                                            <minus/>
                                            <apply>
                                                <times/>
                                                <cn type="integer">4</cn>
                                                <ci>KeqAK</ci>
                                            </apply>
                                            <cn type="integer">1</cn>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <power/>
                                        <ci>SUM_P</ci>
                                        <cn type="integer">2</cn>
                                    </apply>
                                </apply>
                                <cn>0.5</cn>
                            </apply>
                        </apply>
                        <apply>
                            <minus/>
                            <cn type="integer">1</cn>
                            <apply>
                                <times/>
                                <cn type="integer">4</cn>
                                <ci>KeqAK</ci>
                            </apply>
                        </apply>
                    </apply>
                </math>
            </assignmentRule>
            <assignmentRule metaid="metaid_0000082" variable="ATP">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <apply>
                        <divide/>
                        <apply>
                            <minus/>
                            <ci>P</ci>
                            <ci>ADP</ci>
                        </apply>
                        <cn type="integer">2</cn>
                    </apply>
                </math>
            </assignmentRule>
            <assignmentRule metaid="metaid_0000083" variable="AMP">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <apply>
                        <minus/>
                        <apply>
                            <minus/>
                            <ci>SUM_P</ci>
                            <ci>ATP</ci>
                        </apply>
                        <ci>ADP</ci>
                    </apply>
                </math>
            </assignmentRule>
        </listOfRules>
        <listOfReactions>
            <reaction id="vGLK" metaid="metaid_0000025" name="Hexokinase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000025">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.1.2"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00299"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1318"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_772596" species="GLCi"/>
                    <speciesReference metaid="_772609" species="P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_772621" species="G6P"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_772634" species="ATP"/>
                    <modifierSpeciesReference metaid="_772647" species="ADP"/>
                </listOfModifiers>
                <kineticLaw metaid="_772659">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>cytosol</ci>
                                        <ci>VmGLK</ci>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <ci>KmGLKGLCi</ci>
                                        <ci>KmGLKATP</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <minus/>
                                    <apply>
                                        <times/>
                                        <ci>GLCi</ci>
                                        <ci>ATP</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>G6P</ci>
                                            <ci>ADP</ci>
                                        </apply>
                                        <ci>KeqGLK</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <times/>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>GLCi</ci>
                                        <ci>KmGLKGLCi</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>G6P</ci>
                                        <ci>KmGLKG6P</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>ATP</ci>
                                        <ci>KmGLKATP</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>ADP</ci>
                                        <ci>KmGLKADP</ci>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmGLK" metaid="_772671" units="mMpermin" value="226.452"/>
                        <parameter id="KmGLKGLCi" metaid="_772683" units="mM" value="0.08"/>
                        <parameter id="KmGLKATP" metaid="_772695" units="mM" value="0.15"/>
                        <parameter id="KeqGLK" metaid="_772707" units="dimensionless" value="3800"/>
                        <parameter id="KmGLKG6P" metaid="_772719" units="mM" value="30"/>
                        <parameter id="KmGLKADP" metaid="_772731" units="mM" value="0.23"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vPGI" metaid="metaid_0000026" name="Glucose-6-phosphate isomerase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000026">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/5.3.1.9"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00771"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_116"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_772743" species="G6P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_772756" species="F6P"/>
                </listOfProducts>
                <kineticLaw metaid="_772769">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>cytosol</ci>
                                        <ci>VmPGI_2</ci>
                                    </apply>
                                    <ci>KmPGIG6P_2</ci>
                                </apply>
                                <apply>
                                    <minus/>
                                    <ci>G6P</ci>
                                    <apply>
                                        <divide/>
                                        <ci>F6P</ci>
                                        <ci>KeqPGI_2</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <plus/>
                                <cn type="integer">1</cn>
                                <apply>
                                    <divide/>
                                    <ci>G6P</ci>
                                    <ci>KmPGIG6P_2</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <ci>F6P</ci>
                                    <ci>KmPGIF6P_2</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmPGI_2" metaid="_772782" units="mMpermin" value="339.677"/>
                        <parameter id="KmPGIG6P_2" metaid="_772794" units="mM" value="1.4"/>
                        <parameter id="KeqPGI_2" metaid="_772807" units="dimensionless" value="0.314"/>
                        <parameter id="KmPGIF6P_2" metaid="_772819" units="mM" value="0.3"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vGLYCO" metaid="metaid_0000027" name="Glycogen synthesis" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000027">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0005978"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1736"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_772831" species="G6P"/>
                    <speciesReference metaid="_772843" species="P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_772855" species="Glyc"/>
                </listOfProducts>
                <kineticLaw metaid="_772867">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <ci>KGLYCOGEN_3</ci>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="KGLYCOGEN_3" metaid="_772879" units="mMpermin" value="6"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vTreha" metaid="metaid_0000028" name="Trehalose 6-phosphate synthase" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000028">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0005992"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_772891" species="G6P" stoichiometry="2"/>
                    <speciesReference metaid="_772903" species="P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_772915" species="Trh"/>
                </listOfProducts>
                <kineticLaw metaid="_772928">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <ci>KTREHALOSE</ci>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="KTREHALOSE" metaid="_772940" units="mMpermin" value="2.4"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vPFK" metaid="metaid_0000029" name="Phosphofructokinase" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000029">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.1.11"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00756"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_736"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_772953" species="F6P"/>
                    <speciesReference metaid="_772966" species="P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_772979" species="F16P"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_772992" species="AMP"/>
                    <modifierSpeciesReference metaid="_773005" species="ATP"/>
                    <modifierSpeciesReference metaid="_773018" species="F26BP"/>
                </listOfModifiers>
                <kineticLaw metaid="_773032">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>cytosol</ci>
                                <ci>VmPFK</ci>
                                <ci>gR</ci>
                                <apply>
                                    <divide/>
                                    <ci>F6P</ci>
                                    <ci>KmPFKF6P</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <ci>ATP</ci>
                                    <ci>KmPFKATP</ci>
                                </apply>
                                <apply>
                                    <ci>R_PFK</ci>
                                    <ci>KmPFKF6P</ci>
                                    <ci>KmPFKATP</ci>
                                    <ci>gR</ci>
                                    <ci>ATP</ci>
                                    <ci>F6P</ci>
                                </apply>
                            </apply>
                            <apply>
                                <plus/>
                                <apply>
                                    <power/>
                                    <apply>
                                        <ci>R_PFK</ci>
                                        <ci>KmPFKF6P</ci>
                                        <ci>KmPFKATP</ci>
                                        <ci>gR</ci>
                                        <ci>ATP</ci>
                                        <ci>F6P</ci>
                                    </apply>
                                    <cn type="integer">2</cn>
                                </apply>
                                <apply>
                                    <times/>
                                    <apply>
                                        <ci>L_PFK</ci>
                                        <ci>Lzero</ci>
                                        <ci>CiPFKATP</ci>
                                        <ci>KiPFKATP</ci>
                                        <ci>CPFKAMP</ci>
                                        <ci>KPFKAMP</ci>
                                        <ci>CPFKF26BP</ci>
                                        <ci>KPFKF26BP</ci>
                                        <ci>CPFKF16BP</ci>
                                        <ci>KPFKF16BP</ci>
                                        <ci>ATP</ci>
                                        <ci>AMP</ci>
                                        <ci>F16P</ci>
                                        <ci>F26BP</ci>
                                    </apply>
                                    <apply>
                                        <power/>
                                        <apply>
                                            <ci>T_PFK</ci>
                                            <ci>CPFKATP</ci>
                                            <ci>KmPFKATP</ci>
                                            <ci>ATP</ci>
                                        </apply>
                                        <cn type="integer">2</cn>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmPFK" metaid="_773045" units="mMpermin" value="182.903"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vALD" metaid="metaid_0000030" name="Aldolase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000030">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/4.1.2.13"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R01070"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1602"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773058" species="F16P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773071" species="TRIO" stoichiometry="2"/>
                </listOfProducts>
                <kineticLaw metaid="_773084">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>cytosol</ci>
                                        <ci>VmALD</ci>
                                    </apply>
                                    <ci>KmALDF16P</ci>
                                </apply>
                                <apply>
                                    <minus/>
                                    <ci>F16P</ci>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <apply>
                                                <divide/>
                                                <ci>KeqTPI</ci>
                                                <apply>
                                                    <plus/>
                                                    <cn type="integer">1</cn>
                                                    <ci>KeqTPI</ci>
                                                </apply>
                                            </apply>
                                            <ci>TRIO</ci>
                                            <apply>
                                                <divide/>
                                                <cn type="integer">1</cn>
                                                <apply>
                                                    <plus/>
                                                    <cn type="integer">1</cn>
                                                    <ci>KeqTPI</ci>
                                                </apply>
                                            </apply>
                                            <ci>TRIO</ci>
                                        </apply>
                                        <ci>KeqALD</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <plus/>
                                <cn type="integer">1</cn>
                                <apply>
                                    <divide/>
                                    <ci>F16P</ci>
                                    <ci>KmALDF16P</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <apply>
                                            <divide/>
                                            <ci>KeqTPI</ci>
                                            <apply>
                                                <plus/>
                                                <cn type="integer">1</cn>
                                                <ci>KeqTPI</ci>
                                            </apply>
                                        </apply>
                                        <ci>TRIO</ci>
                                    </apply>
                                    <ci>KmALDGAP</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <apply>
                                            <divide/>
                                            <cn type="integer">1</cn>
                                            <apply>
                                                <plus/>
                                                <cn type="integer">1</cn>
                                                <ci>KeqTPI</ci>
                                            </apply>
                                        </apply>
                                        <ci>TRIO</ci>
                                    </apply>
                                    <ci>KmALDDHAP</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <apply>
                                            <divide/>
                                            <ci>KeqTPI</ci>
                                            <apply>
                                                <plus/>
                                                <cn type="integer">1</cn>
                                                <ci>KeqTPI</ci>
                                            </apply>
                                        </apply>
                                        <ci>TRIO</ci>
                                        <apply>
                                            <divide/>
                                            <cn type="integer">1</cn>
                                            <apply>
                                                <plus/>
                                                <cn type="integer">1</cn>
                                                <ci>KeqTPI</ci>
                                            </apply>
                                        </apply>
                                        <ci>TRIO</ci>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <ci>KmALDGAP</ci>
                                        <ci>KmALDDHAP</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>F16P</ci>
                                        <apply>
                                            <divide/>
                                            <ci>KeqTPI</ci>
                                            <apply>
                                                <plus/>
                                                <cn type="integer">1</cn>
                                                <ci>KeqTPI</ci>
                                            </apply>
                                        </apply>
                                        <ci>TRIO</ci>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <ci>KmALDGAPi</ci>
                                        <ci>KmALDF16P</ci>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmALD" metaid="_773097" units="mMpermin" value="322.258"/>
                        <parameter id="KmALDF16P" metaid="_773110" units="mM" value="0.3"/>
                        <parameter id="KeqALD" metaid="_773122" units="dimensionless" value="0.069"/>
                        <parameter id="KmALDGAP" metaid="_773134" units="mM" value="2"/>
                        <parameter id="KmALDDHAP" metaid="_773146" units="mM" value="2.4"/>
                        <parameter id="KmALDGAPi" metaid="_773158" units="mM" value="10"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vGAPDH" metaid="metaid_0000031" name="Glyceraldehyde 3-phosphate dehydrogenase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000031">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/1.2.1.12"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R01061"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1847"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773170" species="TRIO"/>
                    <speciesReference metaid="_773182" species="NAD"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773194" species="BPG"/>
                    <speciesReference metaid="_773206" species="NADH"/>
                </listOfProducts>
                <kineticLaw metaid="_773218">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>cytosol</ci>
                                <apply>
                                    <minus/>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>VmGAPDHf</ci>
                                            <apply>
                                                <divide/>
                                                <ci>KeqTPI</ci>
                                                <apply>
                                                    <plus/>
                                                    <cn type="integer">1</cn>
                                                    <ci>KeqTPI</ci>
                                                </apply>
                                            </apply>
                                            <ci>TRIO</ci>
                                            <ci>NAD</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KmGAPDHGAP</ci>
                                            <ci>KmGAPDHNAD</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>VmGAPDHr</ci>
                                            <ci>BPG</ci>
                                            <ci>NADH</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KmGAPDHBPG</ci>
                                            <ci>KmGAPDHNADH</ci>
                                        </apply>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <times/>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <apply>
                                                <divide/>
                                                <ci>KeqTPI</ci>
                                                <apply>
                                                    <plus/>
                                                    <cn type="integer">1</cn>
                                                    <ci>KeqTPI</ci>
                                                </apply>
                                            </apply>
                                            <ci>TRIO</ci>
                                        </apply>
                                        <ci>KmGAPDHGAP</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>BPG</ci>
                                        <ci>KmGAPDHBPG</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>NAD</ci>
                                        <ci>KmGAPDHNAD</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>NADH</ci>
                                        <ci>KmGAPDHNADH</ci>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmGAPDHf" metaid="_773230" units="mMpermin" value="1184.52"/>
                        <parameter id="KmGAPDHGAP" metaid="_773242" units="mM" value="0.21"/>
                        <parameter id="KmGAPDHNAD" metaid="_773254" units="mM" value="0.09"/>
                        <parameter id="VmGAPDHr" metaid="_773266" units="mMpermin" value="6549.8"/>
                        <parameter id="KmGAPDHBPG" metaid="_773278" units="mM" value="0.0098"/>
                        <parameter id="KmGAPDHNADH" metaid="_773290" units="mM" value="0.06"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vPGK" metaid="metaid_0000032" name="Phosphoglycerate kinase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000032">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.2.3"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R01512"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1771"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773302" species="BPG"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773314" species="P3G"/>
                    <speciesReference metaid="_773326" species="P"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_773338" species="ATP"/>
                    <modifierSpeciesReference metaid="_773350" species="ADP"/>
                </listOfModifiers>
                <kineticLaw metaid="_773362">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>cytosol</ci>
                                        <ci>VmPGK</ci>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <ci>KmPGKP3G</ci>
                                        <ci>KmPGKATP</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <minus/>
                                    <apply>
                                        <times/>
                                        <ci>KeqPGK</ci>
                                        <ci>BPG</ci>
                                        <ci>ADP</ci>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <ci>P3G</ci>
                                        <ci>ATP</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <times/>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>BPG</ci>
                                        <ci>KmPGKBPG</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>P3G</ci>
                                        <ci>KmPGKP3G</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>ATP</ci>
                                        <ci>KmPGKATP</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>ADP</ci>
                                        <ci>KmPGKADP</ci>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmPGK" metaid="_773374" units="mMpermin" value="1306.45"/>
                        <parameter id="KmPGKP3G" metaid="_773386" units="mM" value="0.53"/>
                        <parameter id="KmPGKATP" metaid="_773398" units="mM" value="0.3"/>
                        <parameter id="KeqPGK" metaid="_773410" units="dimensionless" value="3200"/>
                        <parameter id="KmPGKBPG" metaid="_773422" units="mM" value="0.003"/>
                        <parameter id="KmPGKADP" metaid="_773434" units="mM" value="0.2"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vPGM" metaid="metaid_0000033" name="Phosphoglycerate mutase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000033">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/5.4.2.1"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R01518"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_576"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773446" species="P3G"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773458" species="P2G"/>
                </listOfProducts>
                <kineticLaw metaid="_773470">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>cytosol</ci>
                                        <ci>VmPGM</ci>
                                    </apply>
                                    <ci>KmPGMP3G</ci>
                                </apply>
                                <apply>
                                    <minus/>
                                    <ci>P3G</ci>
                                    <apply>
                                        <divide/>
                                        <ci>P2G</ci>
                                        <ci>KeqPGM</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <plus/>
                                <cn type="integer">1</cn>
                                <apply>
                                    <divide/>
                                    <ci>P3G</ci>
                                    <ci>KmPGMP3G</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <ci>P2G</ci>
                                    <ci>KmPGMP2G</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmPGM" metaid="_773482" units="mMpermin" value="2525.81"/>
                        <parameter id="KmPGMP3G" metaid="_773494" units="mM" value="1.2"/>
                        <parameter id="KeqPGM" metaid="_773506" units="dimensionless" value="0.19"/>
                        <parameter id="KmPGMP2G" metaid="_773518" units="mM" value="0.08"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vENO" metaid="metaid_0000034" name="Enolase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000034">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/4.2.1.11"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00658"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1400"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773530" species="P2G"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773542" species="PEP"/>
                </listOfProducts>
                <kineticLaw metaid="_773554">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>cytosol</ci>
                                        <ci>VmENO</ci>
                                    </apply>
                                    <ci>KmENOP2G</ci>
                                </apply>
                                <apply>
                                    <minus/>
                                    <ci>P2G</ci>
                                    <apply>
                                        <divide/>
                                        <ci>PEP</ci>
                                        <ci>KeqENO</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <plus/>
                                <cn type="integer">1</cn>
                                <apply>
                                    <divide/>
                                    <ci>P2G</ci>
                                    <ci>KmENOP2G</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <ci>PEP</ci>
                                    <ci>KmENOPEP</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmENO" metaid="_773566" units="mMpermin" value="365.806"/>
                        <parameter id="KmENOP2G" metaid="_773578" units="mM" value="0.04"/>
                        <parameter id="KeqENO" metaid="_773590" units="dimensionless" value="6.7"/>
                        <parameter id="KmENOPEP" metaid="_773602" units="mM" value="0.5"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vPYK" metaid="metaid_0000035" name="Pyruvate kinase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000035">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.1.40"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00200"/>
                                </rdf:Bag>
                            </bqbiol:is>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1911"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773614" species="PEP"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773626" species="PYR"/>
                    <speciesReference metaid="_773638" species="P"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_773650" species="ATP"/>
                    <modifierSpeciesReference metaid="_773662" species="ADP"/>
                </listOfModifiers>
                <kineticLaw metaid="_773674">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>cytosol</ci>
                                        <ci>VmPYK</ci>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <ci>KmPYKPEP</ci>
                                        <ci>KmPYKADP</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <minus/>
                                    <apply>
                                        <times/>
                                        <ci>PEP</ci>
                                        <ci>ADP</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>PYR</ci>
                                            <ci>ATP</ci>
                                        </apply>
                                        <ci>KeqPYK</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <times/>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>PEP</ci>
                                        <ci>KmPYKPEP</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>PYR</ci>
                                        <ci>KmPYKPYR</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>ATP</ci>
                                        <ci>KmPYKATP</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>ADP</ci>
                                        <ci>KmPYKADP</ci>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmPYK" metaid="_773686" units="mMpermin" value="1088.71"/>
                        <parameter id="KmPYKPEP" metaid="_773698" units="mM" value="0.14"/>
                        <parameter id="KmPYKADP" metaid="_773710" units="mM" value="0.53"/>
                        <parameter id="KeqPYK" metaid="_773722" units="dimensionless" value="6500"/>
                        <parameter id="KmPYKPYR" metaid="_773734" units="mM" value="21"/>
                        <parameter id="KmPYKATP" metaid="_773746" units="mM" value="1.5"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vPDC" metaid="metaid_0000036" name="Pyruvate decarboxylase" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000036">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/4.1.1.1"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00224"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773758" species="PYR"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773770" species="ACE"/>
                    <speciesReference metaid="_773782" species="CO2"/>
                </listOfProducts>
                <kineticLaw metaid="_773794">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>cytosol</ci>
                                <ci>VmPDC</ci>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <power/>
                                        <ci>PYR</ci>
                                        <ci>nPDC</ci>
                                    </apply>
                                    <apply>
                                        <power/>
                                        <ci>KmPDCPYR</ci>
                                        <ci>nPDC</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <plus/>
                                <cn type="integer">1</cn>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <power/>
                                        <ci>PYR</ci>
                                        <ci>nPDC</ci>
                                    </apply>
                                    <apply>
                                        <power/>
                                        <ci>KmPDCPYR</ci>
                                        <ci>nPDC</ci>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmPDC" metaid="_773806" units="mMpermin" value="174.194"/>
                        <parameter id="nPDC" metaid="_773818" units="dimensionless" value="1.9"/>
                        <parameter id="KmPDCPYR" metaid="_773831" units="mM" value="4.33"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vSUC" metaid="metaid_0000037" name="Succinate synthesis" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000037">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0006105"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773843" species="ACE" stoichiometry="2"/>
                    <speciesReference metaid="_773855" species="NAD" stoichiometry="3"/>
                    <speciesReference metaid="_773867" species="P" stoichiometry="4"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773879" species="NADH" stoichiometry="3"/>
                    <speciesReference metaid="_773891" species="SUCC"/>
                </listOfProducts>
                <kineticLaw metaid="_773903">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <ci>KSUCC</ci>
                            <ci>ACE</ci>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="KSUCC" metaid="_773915" value="21.4"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vGLT" metaid="metaid_0000038" name="Glucose transport">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000038">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0046323"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_2092"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_773927" species="GLCo"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_773939" species="GLCi"/>
                </listOfProducts>
                <kineticLaw metaid="_773951">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <ci>VmGLT</ci>
                                    <ci>KmGLTGLCo</ci>
                                </apply>
                                <apply>
                                    <minus/>
                                    <ci>GLCo</ci>
                                    <apply>
                                        <divide/>
                                        <ci>GLCi</ci>
                                        <ci>KeqGLT</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <plus/>
                                <cn type="integer">1</cn>
                                <apply>
                                    <divide/>
                                    <ci>GLCo</ci>
                                    <ci>KmGLTGLCo</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <ci>GLCi</ci>
                                    <ci>KmGLTGLCi</ci>
                                </apply>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <cn>0.91</cn>
                                        <ci>GLCo</ci>
                                        <ci>GLCi</ci>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <ci>KmGLTGLCo</ci>
                                        <ci>KmGLTGLCi</ci>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmGLT" metaid="_773963" units="mmolepermin" value="97.264"/>
                        <parameter id="KmGLTGLCo" metaid="_773975" units="mM" value="1.1918"/>
                        <parameter id="KeqGLT" metaid="_773987" units="mM" value="1"/>
                        <parameter id="KmGLTGLCi" metaid="_773999" units="mM" value="1.1918"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vADH" metaid="metaid_0000039" name="Alcohol dehydrogenase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000039">
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_799"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/1.1.1.2"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00746"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_774011" species="ACE"/>
                    <speciesReference metaid="_774023" species="NADH"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_774035" species="NAD"/>
                    <speciesReference metaid="_774047" species="ETOH"/>
                </listOfProducts>
                <kineticLaw metaid="_774059">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <apply>
                                <minus/>
                                <ci>cytosol</ci>
                            </apply>
                            <apply>
                                <divide/>
                                <apply>
                                    <times/>
                                    <apply>
                                        <divide/>
                                        <ci>VmADH</ci>
                                        <apply>
                                            <times/>
                                            <ci>KiADHNAD</ci>
                                            <ci>KmADHETOH</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <minus/>
                                        <apply>
                                            <times/>
                                            <ci>NAD</ci>
                                            <ci>ETOH</ci>
                                        </apply>
                                        <apply>
                                            <divide/>
                                            <apply>
                                                <times/>
                                                <ci>NADH</ci>
                                                <ci>ACE</ci>
                                            </apply>
                                            <ci>KeqADH</ci>
                                        </apply>
                                    </apply>
                                </apply>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>NAD</ci>
                                        <ci>KiADHNAD</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>KmADHNAD</ci>
                                            <ci>ETOH</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KiADHNAD</ci>
                                            <ci>KmADHETOH</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>KmADHNADH</ci>
                                            <ci>ACE</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KiADHNADH</ci>
                                            <ci>KmADHACE</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>NADH</ci>
                                        <ci>KiADHNADH</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>NAD</ci>
                                            <ci>ETOH</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KiADHNAD</ci>
                                            <ci>KmADHETOH</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>KmADHNADH</ci>
                                            <ci>NAD</ci>
                                            <ci>ACE</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KiADHNAD</ci>
                                            <ci>KiADHNADH</ci>
                                            <ci>KmADHACE</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>KmADHNAD</ci>
                                            <ci>ETOH</ci>
                                            <ci>NADH</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KiADHNAD</ci>
                                            <ci>KmADHETOH</ci>
                                            <ci>KiADHNADH</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>NADH</ci>
                                            <ci>ACE</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KiADHNADH</ci>
                                            <ci>KmADHACE</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>NAD</ci>
                                            <ci>ETOH</ci>
                                            <ci>ACE</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KiADHNAD</ci>
                                            <ci>KmADHETOH</ci>
                                            <ci>KiADHACE</ci>
                                        </apply>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>ETOH</ci>
                                            <ci>NADH</ci>
                                            <ci>ACE</ci>
                                        </apply>
                                        <apply>
                                            <times/>
                                            <ci>KiADHETOH</ci>
                                            <ci>KiADHNADH</ci>
                                            <ci>KmADHACE</ci>
                                        </apply>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmADH" metaid="_774071" units="mMpermin" value="810"/>
                        <parameter id="KiADHNAD" metaid="_774083" units="mM" value="0.92"/>
                        <parameter id="KmADHETOH" metaid="_774095" units="mM" value="17"/>
                        <parameter id="KeqADH" metaid="_774107" units="dimensionless" value="6.9E-5"/>
                        <parameter id="KmADHNAD" metaid="_774119" units="mM" value="0.17"/>
                        <parameter id="KmADHNADH" metaid="_774131" units="mM" value="0.11"/>
                        <parameter id="KiADHNADH" metaid="_774143" units="mM" value="0.031"/>
                        <parameter id="KmADHACE" metaid="_774155" units="mM" value="1.11"/>
                        <parameter id="KiADHACE" metaid="_774167" units="mM" value="1.1"/>
                        <parameter id="KiADHETOH" metaid="_774179" units="mM" value="90"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vG3PDH" metaid="metaid_0000040" name="Glycerol 3-phosphate dehydrogenase" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000040">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/1.1.1.8"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_774191" species="TRIO"/>
                    <speciesReference metaid="_774204" species="NADH"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_774216" species="NAD"/>
                    <speciesReference metaid="_774228" species="GLY"/>
                </listOfProducts>
                <kineticLaw metaid="_774240">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <apply>
                                    <divide/>
                                    <apply>
                                        <times/>
                                        <ci>cytosol</ci>
                                        <ci>VmG3PDH</ci>
                                    </apply>
                                    <apply>
                                        <times/>
                                        <ci>KmG3PDHDHAP</ci>
                                        <ci>KmG3PDHNADH</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <minus/>
                                    <apply>
                                        <times/>
                                        <apply>
                                            <divide/>
                                            <cn type="integer">1</cn>
                                            <apply>
                                                <plus/>
                                                <cn type="integer">1</cn>
                                                <ci>KeqTPI</ci>
                                            </apply>
                                        </apply>
                                        <ci>TRIO</ci>
                                        <ci>NADH</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <ci>GLY</ci>
                                            <ci>NAD</ci>
                                        </apply>
                                        <ci>KeqG3PDH</ci>
                                    </apply>
                                </apply>
                            </apply>
                            <apply>
                                <times/>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <apply>
                                            <times/>
                                            <apply>
                                                <divide/>
                                                <cn type="integer">1</cn>
                                                <apply>
                                                    <plus/>
                                                    <cn type="integer">1</cn>
                                                    <ci>KeqTPI</ci>
                                                </apply>
                                            </apply>
                                            <ci>TRIO</ci>
                                        </apply>
                                        <ci>KmG3PDHDHAP</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>GLY</ci>
                                        <ci>KmG3PDHGLY</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <divide/>
                                        <ci>NADH</ci>
                                        <ci>KmG3PDHNADH</ci>
                                    </apply>
                                    <apply>
                                        <divide/>
                                        <ci>NAD</ci>
                                        <ci>KmG3PDHNAD</ci>
                                    </apply>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="VmG3PDH" metaid="_774252" units="mMpermin" value="70.15"/>
                        <parameter id="KmG3PDHDHAP" metaid="_774264" units="mM" value="0.4"/>
                        <parameter id="KmG3PDHNADH" metaid="_774276" units="mM" value="0.023"/>
                        <parameter id="KeqG3PDH" metaid="_774288" units="dimensionless" value="4300"/>
                        <parameter id="KmG3PDHGLY" metaid="_774300" units="mM" value="1"/>
                        <parameter id="KmG3PDHNAD" metaid="_774312" units="mM" value="0.93"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="vATP" metaid="metaid_0000041" name="ATPase activity">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000041">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/3.6.1.3"/>
                                    <rdf:li rdf:resource="http://identifiers.org/obo.go/GO:0016887"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_774324" species="P"/>
                </listOfReactants>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_774336" species="ATP"/>
                </listOfModifiers>
                <kineticLaw metaid="_774348">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <ci>KATPASE</ci>
                            <ci>ATP</ci>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="KATPASE" metaid="_774360" units="permin" value="33.7"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
        </listOfReactions>
    </model>
</sbml>
""".encode('utf-8')