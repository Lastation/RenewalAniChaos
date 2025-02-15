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
         if (v.P_LoopMain[playerID] < 6) 
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            x = 75 - 32 * v.P_LoopMain[playerID];
            y = 100;

            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", x, y);
            trg.Shape_Square(playerID, 1, "Scantid (Desert)", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID);
         }
         
         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 6)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}