import variable as v;
import func.trig as trg;
import func.trigepic as epic;

var d = 0;

function main(playerID)
{
   MoveUnit(All, "60 + 1n Dragoon", playerID, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n High Templar", playerID, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "50 + 1n Tank", playerID, "Anywhere", "[Skill]HoldPosition");

   trg.Debuff_BanReturn();
   trg.Debuff_Stop();

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         d = 75 + 75 * v.P_LoopMain[playerID];

         if (v.P_LoopMain[playerID] < 3)
         {
            if (v.P_LoopMain[playerID] == 0) 
            {
               trg.Shape_Dot(playerID, 1, "40 + 1n Gantrithor", 0, 0);
            }

            trg.Shape_Edge(playerID, 1, "40 + 1n Gantrithor", 45, 3 + 2 * v.P_LoopMain[playerID], d);
            trg.Shape_Edge(playerID, 1, "60 + 1n Archon", 45, 3 + 2 * v.P_LoopMain[playerID], d);

            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         if (v.P_LoopMain[playerID] == 0)
         {          
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 64, 0);
            trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 32, 32);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("60 + 1n High Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {          
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 128, 0);
            trg.Shape_Square(playerID, 1, "50 + 1n Tank", 64, 64);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {          
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 160, 96);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 160, 160);
            trg.Shape_Square(playerID, 1, "60 + 1n Siege", 96, 160);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 28)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}