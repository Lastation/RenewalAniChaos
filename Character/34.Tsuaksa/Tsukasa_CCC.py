import variable as v;
import func.trig as trg;
import func.trigepic as epic;

var x = 0;
var y = 0;

var d = 0;
var i = 0;

var t = 0;

function main(playerID)
{
   MoveUnit(All, "60 + 1n Dragoon", playerID, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n High Templar", playerID, "Anywhere", "[Skill]HoldPosition");

   trg.Debuff_BanReturn();
   trg.Debuff_Stop();

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         d = 64 - 16 * v.P_LoopMain[playerID];

         trg.Table_Sin(playerID, 30 *  v.P_LoopMain[playerID], d);
         trg.Table_Cos(playerID, 30 *  v.P_LoopMain[playerID], d);

         x = v.P_AngleCos[playerID];
         y = v.P_AngleSin[playerID];

         if (v.P_LoopMain[playerID] < 4)
         {          
            trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", x, y);
            trg.Shape_Square(playerID, 6, "Protoss Dark Templar", x, y);

            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 4)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         d = 75 + 75 * v.P_LoopMain[playerID];

         if (v.P_LoopMain[playerID] < 3)
         {
            for (i = 0; i < 3; i++) {
               trg.Table_Sin(playerID, 30 * i, d);
               trg.Table_Cos(playerID, 30 * i, d);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", x, y);
               trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, y);
            }

            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         if (v.P_LoopMain[playerID] == 3)
         {          
            for (i = 0; i < 3; i++) {
               trg.Table_Sin(playerID, 30 * i, 200);
               trg.Table_Cos(playerID, 30 * i, 200);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", x, y);
            }
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 8)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         t = 50;

         if (v.P_LoopMain[playerID] == 0) { x = 0; y = -1; }
         else if (v.P_LoopMain[playerID] == 1) { x = 1; y = -2; }
         else if (v.P_LoopMain[playerID] == 2) { x = 2; y = -2; }
         else if (v.P_LoopMain[playerID] == 3) { x = 3; y = -1; }
         else if (v.P_LoopMain[playerID] == 4) { x = 3; y = 0; }
         else if (v.P_LoopMain[playerID] == 5) { x = 2; y = 1; }
         else if (v.P_LoopMain[playerID] == 6) { x = 1; y = 2; }
         else if (v.P_LoopMain[playerID] == 7) { x = 0; y = 3; }

         if (v.P_LoopMain[playerID] < 8) {
            epic.Shape_Dot(playerID, 1, "60 + 1n Danimoth", t * x, t * y, 1);
            trg.Shape_Dot(playerID, 1, "60 + 1n High Templar", t * x, t * y);

            if (v.P_LoopMain[playerID] != 0 && v.P_LoopMain[playerID] != 7) {
               epic.Shape_Dot(playerID, 1, "60 + 1n Danimoth", -t * x, t * y, 1);
               trg.Shape_Dot(playerID, 1, "60 + 1n High Templar", -t * x, t * y);
            }

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("60 + 1n High Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 8)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         t = 50;

         if (v.P_LoopMain[playerID] == 0) {
            for (i = 0; i < 8; i++) {
               if (i == 0) { x = 0; y = -1; }
               else if (i == 1) { x = 1; y = -2; }
               else if (i == 2) { x = 2; y = -2; }
               else if (i == 3) { x = 3; y = -1; }
               else if (i == 4) { x = 3; y = 0; }
               else if (i == 5) { x = 2; y = 1; }
               else if (i == 6) { x = 1; y = 2; }
               else if (i == 7) { x = 0; y = 3; }

               if (i < 8) {
                  trg.Shape_Dot(playerID, 1, "40 + 1n Guardian", t * x, t * y);
                  trg.Shape_Dot(playerID, 1, "60 + 1n Archon", t * x, t * y);

                  if (i != 0 && i != 7) {
                     trg.Shape_Dot(playerID, 1, "40 + 1n Guardian", -t * x, t * y);
                     trg.Shape_Dot(playerID, 1, "60 + 1n Archon", -t * x, t * y);
                  }
               }
            }

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1) {
            for (i = 0; i < 8; i++) {
               if (i == 0) { x = 0; y = -1; }
               else if (i == 1) { x = 1; y = -2; }
               else if (i == 2) { x = 2; y = -2; }
               else if (i == 3) { x = 3; y = -1; }
               else if (i == 4) { x = 3; y = 0; }
               else if (i == 5) { x = 2; y = 1; }
               else if (i == 6) { x = 1; y = 2; }
               else if (i == 7) { x = 0; y = 3; }

               if (i < 8) {
                  trg.Shape_Dot(playerID, 1, "Kakaru (Twilight)", t * x, t * y);
                  trg.Shape_Dot(playerID, 1, " Unit. Hoffnung 25000", t * x, t * y);

                  if (i != 0 && i != 7) {
                     trg.Shape_Dot(playerID, 1, "Kakaru (Twilight)", -t * x, t * y);
                     trg.Shape_Dot(playerID, 1, " Unit. Hoffnung 25000", -t * x, t * y);
                  }
               }
            }

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 12)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 4)
      {
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         
         trg.SkillEnd();
      }
   }
}