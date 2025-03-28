import variable as v;
import func.trig as trg;
import func.trigepic as epic;

function main(playerID)
{
   trg.Debuff_Stop();
   trg.Debuff_BanReturn();

   var x;
   var y;

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            trg.Shape_NxNSquare(playerID, 1, " Unit. Hoffnung 25000", 7, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 58) 
         {
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Archon", 4, 75);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 60) 
         {
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Archon", 7, 75);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 61)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1) 
         {
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2) 
         {
            epic.Shape_NxNSquare(playerID, 1, "60 + 1n Danimoth", 7, 75, 1);
            trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 7, 75);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);  

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3) 
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Danimoth", 7, 75);
            trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 7, 75);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);  
            MoveUnit(All, "50 + 1n Tank", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         else if (v.P_LoopMain[playerID] == 5) 
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 7) 
         {
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 14)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         if (v.P_LoopMain[playerID] == 0)
         {
            trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 0, 6, 160);
            trg.Shape_Edge(playerID, 1, "50 + 1n Battlecruiser", 0, 6, 160);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);      

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {
            trg.Shape_Edge(playerID, 1, "60 + 1n Archon", 0, 6, 160);
            trg.Shape_Edge(playerID, 1, "60 + 1n Danimoth", 0, 6, 160);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);  

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 8)
         {
            trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 45, 6, 160);
            trg.Shape_Edge(playerID, 1, "50 + 1n Battlecruiser", 45, 6, 160);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);      

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);         
         }
         else if (v.P_LoopMain[playerID] == 9)
         {
            trg.Shape_Edge(playerID, 1, "60 + 1n Archon", 45, 6, 160);
            trg.Shape_Edge(playerID, 1, "60 + 1n Danimoth", 45, 6, 160);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);  

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }


         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 15)
         {                        
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         trg.Table_Sin(playerID, 22 + 4 * v.P_LoopMain[playerID], 100 - 4 * v.P_LoopMain[playerID]);
         trg.Table_Cos(playerID, 22 + 4 * v.P_LoopMain[playerID], 100 - 4 * v.P_LoopMain[playerID]);

         x = v.P_AngleCos[playerID];
         y = v.P_AngleSin[playerID];

         trg.Shape_Square(playerID, 1, "60 + 1n High Templar", x, y);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 13)
         {              
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 4)
      {
         if (v.P_LoopMain[playerID] == 0)
         {
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Siege", 5, 75);
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Danimoth", 5, 75);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);    

            KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {
            trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 5, 75);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);            
         }
         else if (v.P_LoopMain[playerID] == 2)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Shape_Edge(playerID, 1, "60 + 1n Danimoth", 45, 7, 225);
            trg.Shape_Edge(playerID, 1, "60 + 1n Danimoth", 45, 9, 300);
            trg.Shape_Edge(playerID, 1, "60 + 1n Siege", 45, 7, 225);
            trg.Shape_Edge(playerID, 1, "60 + 1n Siege", 45, 9, 300);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);    

            KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {
            trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 45, 7, 225);
            trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 45, 9, 300);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);  
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 5)
         {                        
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 5)
      {
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

         trg.SkillEnd();    
      }
   }
}