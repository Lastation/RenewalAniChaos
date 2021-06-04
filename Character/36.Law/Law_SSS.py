import variable as v;
import func.trig as trg;

function main(playerID)
{
   var x;
   var y;

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            trg.Shape_Edge(playerID, 1, "40 + 1n Wraith", 45, 3, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {
            trg.Shape_Edge(playerID, 1, "40 + 1n Wraith", 45, 4, 120);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {
            trg.Shape_Edge(playerID, 1, "50 + 1n Battlecruiser", 45, 3, 120);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 45, 3, 120);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         } 

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 7)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] < 8) 
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            trg.Table_Sin(playerID, 22 *  v.P_LoopMain[playerID], 32);
            trg.Table_Cos(playerID, 22 *  v.P_LoopMain[playerID], 32);

            x = v.P_AngleCos[playerID];
            y = v.P_AngleSin[playerID];

            trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", x, y);
            trg.Shape_Dot(playerID, 1, "40 + 1n Mojo", x, y);

            trg.Shape_Double(playerID, 1, "Scantid (Desert)", x, y);

            trg.Table_Sin(playerID, 22 *  v.P_LoopMain[playerID], 64);
            trg.Table_Cos(playerID, 22 *  v.P_LoopMain[playerID], 64);

            x = v.P_AngleCos[playerID];
            y = v.P_AngleSin[playerID];

            trg.Shape_Double(playerID, 1, "Kakaru (Twilight)", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 8)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }

      else if (v.P_CountMain[playerID] == 2)
      {
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}