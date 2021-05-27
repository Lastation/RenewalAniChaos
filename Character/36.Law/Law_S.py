import variable as v;
import func.trig as trg;

function main(playerID)
{
   var x = 50;
   var y = 50;

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", x, y);
            trg.Shape_Square(playerID, 1, "Scantid (Desert)", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", x, y);
            trg.Shape_Square(playerID, 1, "Scantid (Desert)", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
         } 
         else if (v.P_LoopMain[playerID] == 3)
         {
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", x, y);
            trg.Shape_Square(playerID, 1, "Scantid (Desert)", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", x, y);
            trg.Shape_Square(playerID, 1, "Scantid (Desert)", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 5)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}