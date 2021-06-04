import variable as v;
import func.trig as trg;
import func.trigepic as epic;
import func.trigadv as adv;
import func.sound as s;

var x = 0;
var y = 0;

var d = 0;

function main(playerID)
{
   trg.Debuff_BanReturn();
   
   MoveUnit(All, "60 + 1n Hydralisk", playerID, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n Archon", playerID, "Anywhere", "[Skill]HoldPosition");

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         trg.Shape_Edge(playerID, 1, "Protoss Observer", 0, 3 + 1 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID]);
         if (v.P_LoopMain[playerID] % 4 == 0)
         {
            trg.Shape_Edge(playerID, 1, "60 + 1n Hydralisk", 0, 3 + 1 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID]);
         } 
         else if (v.P_LoopMain[playerID] % 4 == 2)
         {
            trg.Shape_Edge(playerID, 1, "60 + 1n Archon", 0, 3 + 1 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID]);
         }

         MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
         Order("60 + 1n Archon", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         Order("60 + 1n Hydralisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 12)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         var d = 30 * v.P_LoopMain[playerID];
         var distance = 300 - 30 * v.P_LoopMain[playerID];

         trg.Table_Sin(playerID, d, distance);
         trg.Table_Cos(playerID, d, distance);
         
         var x = v.P_AngleCos[playerID];
         var y = v.P_AngleSin[playerID];

         adv.Shape_QuadNxNSquareAt(playerID, 1, "80 + 1n Artanis", 2, 50, x, y);
         adv.Shape_QuadNxNSquareAt(playerID, 1, "Scantid (Desert)", 3, 50, x, y);

         MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
         Order("80 + 1n Artanis", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

         KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 8)
         {        
            KillUnitAt(All, "80 + 1n Artanis", "Anywhere", playerID);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         if (v.P_LoopMain[playerID] < 12) 
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mojo", 11, 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 14)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);

         SetSwitch("UiltimateSwitch", Clear);
         trg.SkillEnd();
      }
   }
}
